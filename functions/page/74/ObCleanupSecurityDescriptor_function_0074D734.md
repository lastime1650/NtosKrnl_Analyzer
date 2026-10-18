# ObCleanupSecurityDescriptor

- RVA: `0x0074D734`–`0x0074D772` (길이 `62` bytes)
- VA: `0x000000014074D734`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4794`
- 디코드: `18`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0074D750` → [RtlGetDaclSecurityDescriptor](../../text/45/RtlGetDaclSecurityDescriptor_function_00459570.md) (function, `0x00459570`)
- `0x0074D767` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [ObpInitializeRootNamespace](ObpInitializeRootNamespace_function_0074E588.md) at `0x0074E78D`
- [MiCreatePartitionNamespace](../81/MiCreatePartitionNamespace_function_00811118.md) at `0x00811215`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0074D750` → [RtlGetDaclSecurityDescriptor](../../text/45/RtlGetDaclSecurityDescriptor_function_00459570.md) (`PAGE` → `.text`)
  - `0x0074D767` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074D734  48 8B C4                        mov rax, rsp
0074D737  48 83 EC 28                     sub rsp, 0x28
0074D73B  48 83 60 20 00                  and qword ptr [rax + 0x20], 0
0074D740  4C 8D 48 18                     lea r9, [rax + 0x18]
0074D744  4C 8D 40 20                     lea r8, [rax + 0x20]
0074D748  C6 40 10 00                     mov byte ptr [rax + 0x10], 0
0074D74C  48 8D 50 10                     lea rdx, [rax + 0x10]
0074D750  E8 1B BE D0 FF                  call 0x140459570
0074D755  85 C0                           test eax, eax
0074D757  78 13                           js 0x14074d76c
0074D759  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
0074D75E  74 0C                           je 0x14074d76c
0074D760  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0074D765  33 D2                           xor edx, edx
0074D767  E8 04 51 43 00                  call 0x140b82870
0074D76C  48 83 C4 28                     add rsp, 0x28
0074D770  C3                              ret
0074D771  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObCleanupSecurityDescriptor(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int8 *)(v_rsp + 16) = 0;
    result = RtlGetDaclSecurityDescriptor(a1, v_rsp + 16, v_rsp + 32, v_rsp + 24);
    if (sign_flag) goto loc_0074D76C;
    if (v_stack_p10 != 0) {
        a1 = v_stack_p20;
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, v_rsp + 32, v_rsp + 24);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void ObCleanupSecurityDescriptor(void)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_p10;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (40);
    *(uint8_t *)(local_rsp + 0x10) = 0;
    result = RtlGetDaclSecurityDescriptor(a1, local_rsp + 16, local_rsp + 32, local_rsp + 24);
    if (sign_flag) goto loc_0074D76C;
    if (v_stack_p10 != 0) {
        a1 = v_stack_p20;
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, local_rsp + 32, local_rsp + 24);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074D734&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0074D734[BB_0074D734]
  bb_0074D759[BB_0074D759]
  bb_0074D760[BB_0074D760]
  bb_0074D76C[BB_0074D76C]
  bb_0074D771[BB_0074D771]
  bb_0074D734 -->|branch| bb_0074D76C
  bb_0074D734 -->|fallthrough| bb_0074D759
  bb_0074D759 -->|branch| bb_0074D76C
  bb_0074D759 -->|fallthrough| bb_0074D760
  bb_0074D760 -->|flow| bb_0074D76C
```
