# PspPicoSetContextThreadEx

- RVA: `0x00787650`–`0x0078766C` (길이 `28` bytes)
- VA: `0x0000000140787650`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `9`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00787661` → [PspSetContextThreadInternal](../8D/PspSetContextThreadInternal_function_008D4420.md) (function, `0x008D4420`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00787650  48 83 EC 38                     sub rsp, 0x38
00787654  33 C0                           xor eax, eax
00787656  38 44 24 60                     cmp byte ptr [rsp + 0x60], al
0078765A  0F 95 C0                        setne al
0078765D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00787661  E8 BA CD 14 00                  call 0x1408d4420
00787666  48 83 C4 38                     add rsp, 0x38
0078766A  C3                              ret
0078766B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspPicoSetContextThreadEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = 0;
    result = (a5 != 0) ? 1 : 0;
    v_stack_m18 = (unsigned int)(result);
    result = PspSetContextThreadInternal(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspPicoSetContextThreadEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = 0;
    result = (Arg5 != 0) ? 1 : 0;
    v_stack_m18 = (uint32_t)(result);
    result = PspSetContextThreadInternal(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00787650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00787650[BB_00787650]
  bb_0078766B[BB_0078766B]
```
