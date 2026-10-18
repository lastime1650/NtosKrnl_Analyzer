# MiReturnSystemImageAddress

- RVA: `0x00A7F190`–`0x00A7F1AD` (길이 `29` bytes)
- VA: `0x0000000140A7F190`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A7F19A` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x00A7F1A2` → [MiReleaseDriverPtes](MiReleaseDriverPtes_function_00A7F1B4.md) (function, `0x00A7F1B4`)

### Direct callers
- [sub_00988C72](../98/Unknown_function_00988C72.md) at `0x00988C8D`
- [MiGetSystemAddressForImage](MiGetSystemAddressForImage_function_00A74EEC.md) at `0x00A750B1`
- [MiUnloadSystemImage](../AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA3432`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A7F19A` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A7F190  48 83 EC 28                     sub rsp, 0x28
00A7F194  48 C1 EA 0C                     shr rdx, 0xc
00A7F198  8B D2                           mov edx, edx
00A7F19A  E8 91 EF 9B FF                  call 0x14043e130
00A7F19F  48 8B C8                        mov rcx, rax
00A7F1A2  E8 0D 00 00 00                  call 0x140a7f1b4
00A7F1A7  48 83 C4 28                     add rsp, 0x28
00A7F1AB  C3                              ret
00A7F1AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReturnSystemImageAddress(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (a2) >> (12);
    result = MiGetPteAddress(a1, (unsigned int)((unsigned int)(a2)), a3, a4);
    result = MiReleaseDriverPtes(result, (unsigned int)((unsigned int)(a2)), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReturnSystemImageAddress(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (Arg2) >> (12);
    result = MiGetPteAddress(Arg1, (uint32_t)((uint32_t)(Arg2)), a3, a4);
    result = MiReleaseDriverPtes(result, (uint32_t)((uint32_t)(Arg2)), a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A7F190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A7F190[BB_00A7F190]
  bb_00A7F1AC[BB_00A7F1AC]
```
