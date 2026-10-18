# CmpProtectPool

- RVA: `0x00267BB8`–`0x00267BD0` (길이 `24` bytes)
- VA: `0x0000000140267BB8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00267BC5` → [ExProtectPoolEx](ExProtectPoolEx_function_002695D8.md) (function, `0x002695D8`)

### Direct callers
- [HvpFreeBin](../../page/A8/HvpFreeBin_function_00A8158C.md) at `0x00A815BA`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C15B9D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00267BB8  48 83 EC 28                     sub rsp, 0x28
00267BBC  45 8B C8                        mov r9d, r8d
00267BBF  4C 8B C2                        mov r8, rdx
00267BC2  48 8B D1                        mov rdx, rcx
00267BC5  E8 0E 1A 00 00                  call 0x1402695d8
00267BCA  48 83 C4 28                     add rsp, 0x28
00267BCE  C3                              ret
00267BCF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpProtectPool(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExProtectPoolEx(a1, a1, a2, (unsigned int)(a3));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpProtectPool(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExProtectPoolEx(Arg1, Arg1, Arg2, (uint32_t)(Arg3));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00267BB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00267BB8[BB_00267BB8]
  bb_00267BCF[BB_00267BCF]
```
