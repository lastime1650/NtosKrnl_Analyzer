# RtlGetDefaultCodePage

- RVA: `0x00AA5AE0`–`0x00AA5B08` (길이 `40` bytes)
- VA: `0x0000000140AA5AE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AA5AE7` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AA5AE7` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA5AE0  48 83 EC 28                     sub rsp, 0x28
00AA5AE4  4C 8B C9                        mov r9, rcx
00AA5AE7  E8 04 87 85 FF                  call 0x1402fe1f0
00AA5AEC  44 0F B7 80 08 04 00 00         movzx r8d, word ptr [rax + 0x408]
00AA5AF4  66 45 89 01                     mov word ptr [r9], r8w
00AA5AF8  0F B7 80 48 04 00 00            movzx eax, word ptr [rax + 0x448]
00AA5AFF  66 89 02                        mov word ptr [rdx], ax
00AA5B02  48 83 C4 28                     add rsp, 0x28
00AA5B06  C3                              ret
00AA5B07  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGetDefaultCodePage(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a1);
    *(unsigned __int16 *)(a1) = (unsigned __int16)(*(unsigned __int16 *)(result + 1032));
    *(unsigned __int16 *)(a2) = (unsigned __int16)(*(unsigned __int16 *)(result + 1096));
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int16 *)(result + 1096);
}
```

## 5. (Beta) C Style

```c
int64_t RtlGetDefaultCodePage(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, a3, Arg1);
    *(uint16_t *)(Arg1) = (uint16_t)(*(uint16_t *)(result + 0x408));
    *(uint16_t *)(Arg2) = (uint16_t)(*(uint16_t *)(result + 0x448));
    local_rsp = (local_rsp) + (40);
    return *(uint16_t *)(result + 0x448);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA5AE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA5AE0[BB_00AA5AE0]
  bb_00AA5B07[BB_00AA5B07]
```
