# KeSelectInitialIdealProcessorForThread

- RVA: `0x003C294C`–`0x003C299A` (길이 `78` bytes)
- VA: `0x00000001403C294C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `19`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003C298B` → [KeSelectIdealProcessor](../2C/KeSelectIdealProcessor_function_002CE8CC.md) (function, `0x002CE8CC`)

### Direct callers
- [KeStartThread](KeStartThread_function_003C21B8.md) at `0x003C232B`
- [PspAllocateThread](../../page/9E/PspAllocateThread_function_009EF72C.md) at `0x009F01C4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C294C  48 83 EC 28                     sub rsp, 0x28
003C2950  4C 8B 81 B8 00 00 00            mov r8, qword ptr [rcx + 0xb8]
003C2957  4C 8B D2                        mov r10, rdx
003C295A  0F B7 4A 08                     movzx ecx, word ptr [rdx + 8]
003C295E  66 41 3B 88 D0 00 00 00         cmp cx, word ptr [r8 + 0xd0]
003C2966  73 2E                           jae 0x1403c2996
003C2968  49 8B 84 C8 D8 00 00 00         mov rax, qword ptr [r8 + rcx*8 + 0xd8]
003C2970  49 83 C0 10                     add r8, 0x10
003C2974  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003C2979  41 B9 01 00 00 00               mov r9d, 1
003C297F  49 8D 14 48                     lea rdx, [r8 + rcx*2]
003C2983  49 8B CA                        mov rcx, r10
003C2986  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
003C298B  E8 3C BF F0 FF                  call 0x1402ce8cc
003C2990  48 83 C4 28                     add rsp, 0x28
003C2994  C3                              ret
003C2995  CC                              int3
003C2996  33 C0                           xor eax, eax
003C2998  EB D6                           jmp 0x1403c2970
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSelectInitialIdealProcessorForThread(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 8))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + 208))) goto loc_003C2996;
loc_003C2970:
    a3 = (*(unsigned __int64 *)(a1 + 184)) + (16);
    v_stack_p8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + *(unsigned __int16 *)(a2 + 8) * 8 + 216);
    result = KeSelectIdealProcessor(a2, a3 + *(unsigned __int16 *)(a2 + 8) * 2, v_stack_p8, 1);
    v_rsp = (v_rsp) + (40);
    return result;
loc_003C2996:
    result = 0;
    goto loc_003C2970;
}
```

## 5. (Beta) C Style

```c
int64_t KeSelectInitialIdealProcessorForThread(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x8))) >= (*(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + 0xD0))) goto loc_003C2996;
loc_003C2970:
    a3 = (*(uint64_t *)(arg1 + 0xB8)) + (16);
    v_stack_p8 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + *(uint16_t *)(arg2 + 0x8) * 8 + 0xD8);
    result = KeSelectIdealProcessor(Arg2, a3 + *(uint16_t *)(arg2 + 0x8) * 2, v_stack_p8, 1);
    local_rsp = (local_rsp) + (40);
    return result;
loc_003C2996:
    result = 0;
    goto loc_003C2970;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C294C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003C294C[BB_003C294C]
  bb_003C2968[BB_003C2968]
  bb_003C2970[BB_003C2970]
  bb_003C2995[BB_003C2995]
  bb_003C2996[BB_003C2996]
  bb_003C294C -->|branch| bb_003C2996
  bb_003C294C -->|fallthrough| bb_003C2968
  bb_003C2968 -->|flow| bb_003C2970
  bb_003C2995 -->|flow| bb_003C2996
  bb_003C2996 -->|branch| bb_003C2970
```
