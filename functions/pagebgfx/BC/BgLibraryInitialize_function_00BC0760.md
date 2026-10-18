# BgLibraryInitialize

- RVA: `0x00BC0760`–`0x00BC0783` (길이 `35` bytes)
- VA: `0x0000000140BC0760`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC0778` → [BgpFwLibraryInitialize](BgpFwLibraryInitialize_function_00BC5400.md) (function, `0x00BC5400`)

### Direct callers
- [PopInvokeSystemStateHandler](../../pagelk/B7/PopInvokeSystemStateHandler_function_00B76A6C.md) at `0x00B77215`
- [PopRestoreHiberContext](../../pagelk/B7/PopRestoreHiberContext_function_00B777F0.md) at `0x00B77871`
- [BgkInitialize](../../init/C8/BgkInitialize_function_00C80488.md) at `0x00C804E6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC0760  48 83 EC 28                     sub rsp, 0x28
00BC0764  83 FA FF                        cmp edx, -1
00BC0767  74 0F                           je 0x140bc0778
00BC0769  44 0F 20 C0                     mov rax, cr8
00BC076D  3C 02                           cmp al, 2
00BC076F  76 07                           jbe 0x140bc0778
00BC0771  B8 01 00 00 C0                  mov eax, 0xc0000001
00BC0776  EB 05                           jmp 0x140bc077d
00BC0778  E8 83 4C 00 00                  call 0x140bc5400
00BC077D  48 83 C4 28                     add rsp, 0x28
00BC0781  C3                              ret
00BC0782  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgLibraryInitialize(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == -1) goto loc_00BC0778;
    if (((unsigned __int8)(v_cr8)) <= 2) goto loc_00BC0778;
    goto loc_00BC077D;
loc_00BC0778:
    result = BgpFwLibraryInitialize(a1, a2, a3, a4);
loc_00BC077D:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t BgLibraryInitialize(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == -1) goto loc_00BC0778;
    if (((uint8_t)(v_cr8)) <= 2) goto loc_00BC0778;
    goto loc_00BC077D;
loc_00BC0778:
    result = BgpFwLibraryInitialize(Arg1, Arg2, a3, a4);
loc_00BC077D:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC0760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC0760[BB_00BC0760]
  bb_00BC0769[BB_00BC0769]
  bb_00BC0771[BB_00BC0771]
  bb_00BC0778[BB_00BC0778]
  bb_00BC077D[BB_00BC077D]
  bb_00BC0782[BB_00BC0782]
  bb_00BC0760 -->|branch| bb_00BC0778
  bb_00BC0760 -->|fallthrough| bb_00BC0769
  bb_00BC0769 -->|branch| bb_00BC0778
  bb_00BC0769 -->|fallthrough| bb_00BC0771
  bb_00BC0771 -->|branch| bb_00BC077D
  bb_00BC0778 -->|flow| bb_00BC077D
```
