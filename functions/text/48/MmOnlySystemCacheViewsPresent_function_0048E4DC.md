# MmOnlySystemCacheViewsPresent

- RVA: `0x0048E4DC`–`0x0048E51F` (길이 `67` bytes)
- VA: `0x000000014048E4DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BAC`
- 디코드: `21`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0048E4F1` → [MiLockSectionControlArea](../2B/MiLockSectionControlArea_function_002BC930.md) (function, `0x002BC930`)
- `0x0048E50D` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [CcCoherencyFlushAndPurgeCache](CcCoherencyFlushAndPurgeCache_function_0048E3D0.md) at `0x0048E473`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048E4DC  40 53                           push rbx
0048E4DE  48 83 EC 20                     sub rsp, 0x20
0048E4E2  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0048E4E7  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
0048E4EC  BA 01 00 00 00                  mov edx, 1
0048E4F1  E8 3A E4 E2 FF                  call 0x1402bc930
0048E4F6  48 85 C0                        test rax, rax
0048E4F9  74 20                           je 0x14048e51b
0048E4FB  8B 48 58                        mov ecx, dword ptr [rax + 0x58]
0048E4FE  48 39 48 28                     cmp qword ptr [rax + 0x28], rcx
0048E502  48 8D 48 48                     lea rcx, [rax + 0x48]
0048E506  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
0048E50A  0F 94 C3                        sete bl
0048E50D  E8 AE 9D DB FF                  call 0x1402482c0
0048E512  8A C3                           mov al, bl
0048E514  48 83 C4 20                     add rsp, 0x20
0048E518  5B                              pop rbx
0048E519  C3                              ret
0048E51A  CC                              int3
0048E51B  B0 01                           mov al, 1
0048E51D  EB F5                           jmp 0x14048e514
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmOnlySystemCacheViewsPresent(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_stack_p8 = 0;
    result = MiLockSectionControlArea(a1, 1, v_stack_p8, a4);
    if (result == 0) goto loc_0048E51B;
    v_rbx = ((*(unsigned __int64 *)(result + 40)) == ((unsigned int)(*(unsigned int *)(result + 88)))) ? 1 : 0;
    result = MiReleaseSpinLockExclusive(result + 72, v_stack_p8, v_stack_p8, a4);
loc_0048E514:
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rbx);
loc_0048E51B:
    goto loc_0048E514;
}
```

## 5. (Beta) C Style

```c
void MmOnlySystemCacheViewsPresent(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    v_stack_p8 = 0;
    result = MiLockSectionControlArea(a1, 1, v_stack_p8, a4);
    if (result == 0) goto loc_0048E51B;
    local_rbx = ((*(uint64_t *)(result + 0x28)) == ((uint32_t)(*(uint32_t *)(result + 0x58)))) ? 1 : 0;
    result = MiReleaseSpinLockExclusive(result + 72, v_stack_p8, v_stack_p8, a4);
loc_0048E514:
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rbx);
loc_0048E51B:
    goto loc_0048E514;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048E4DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048E4DC[BB_0048E4DC]
  bb_0048E4FB[BB_0048E4FB]
  bb_0048E514[BB_0048E514]
  bb_0048E51A[BB_0048E51A]
  bb_0048E51B[BB_0048E51B]
  bb_0048E4DC -->|branch| bb_0048E51B
  bb_0048E4DC -->|fallthrough| bb_0048E4FB
  bb_0048E4FB -->|flow| bb_0048E514
  bb_0048E51A -->|flow| bb_0048E51B
  bb_0048E51B -->|branch| bb_0048E514
```
