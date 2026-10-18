# PpmIdleGuestExecute

- RVA: `0x004BD260`–`0x004BD28B` (길이 `43` bytes)
- VA: `0x00000001404BD260`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBE1C`
- 디코드: `14`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BD269` → [HalProcessorIdle](../6A/HalProcessorIdle_function_006AC7C0.md) (function, `0x006AC7C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BD260  48 83 EC 38                     sub rsp, 0x38
004BD264  45 85 C0                        test r8d, r8d
004BD267  75 0D                           jne 0x1404bd276
004BD269  E8 52 F5 1E 00                  call 0x1406ac7c0
004BD26E  33 C0                           xor eax, eax
004BD270  48 83 C4 38                     add rsp, 0x38
004BD274  C3                              ret
004BD275  CC                              int3
004BD276  B9 F0 00 00 40                  mov ecx, 0x400000f0
004BD27B  0F 32                           rdmsr
004BD27D  48 C1 E2 20                     shl rdx, 0x20
004BD281  48 0B C2                        or rax, rdx
004BD284  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004BD289  EB E3                           jmp 0x1404bd26e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmIdleGuestExecute(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (56);
    if (a3 != 0) goto loc_004BD276;
    result = HalProcessorIdle(a1, a2, a3, a4);
loc_004BD26E:
    result = 0;
    v_rsp = (v_rsp) + (56);
    return result;
loc_004BD276:
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_p20 = result;
    goto loc_004BD26E;
}
```

## 5. (Beta) C Style

```c
int64_t PpmIdleGuestExecute(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (56);
    if (Arg3 != 0) goto loc_004BD276;
    result = HalProcessorIdle(Arg1, Arg2, Arg3, a4);
loc_004BD26E:
    result = 0;
    local_rsp = (local_rsp) + (56);
    return result;
loc_004BD276:
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_p20 = result;
    goto loc_004BD26E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BD260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BD260[BB_004BD260]
  bb_004BD269[BB_004BD269]
  bb_004BD26E[BB_004BD26E]
  bb_004BD275[BB_004BD275]
  bb_004BD276[BB_004BD276]
  bb_004BD260 -->|branch| bb_004BD276
  bb_004BD260 -->|fallthrough| bb_004BD269
  bb_004BD269 -->|flow| bb_004BD26E
  bb_004BD275 -->|flow| bb_004BD276
  bb_004BD276 -->|branch| bb_004BD26E
```
