# MiSanitizePage

- RVA: `0x00471BF0`–`0x00471C16` (길이 `38` bytes)
- VA: `0x0000000140471BF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiMapContiguousMemory](../32/MiMapContiguousMemory_function_0032787C.md) at `0x00327950`
- [MiMapViewOfPhysicalSection](../../page/97/MiMapViewOfPhysicalSection_function_0097F984.md) at `0x0097FA52`
- [MiMapLockedPagesInUserSpace](../../page/97/MiMapLockedPagesInUserSpace_function_0097FE04.md) at `0x00980043`
- [MiRotateToFrameBuffer](../../page/A3/MiRotateToFrameBuffer_function_00A38214.md) at `0x00A382AC`
- [MiRotateToFrameBufferNoCopy](../../page/A3/MiRotateToFrameBufferNoCopy_function_00A38530.md) at `0x00A385CD`

### Static image references
- `0x00471BF8` → RVA `0x00E2DC38` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00471BF0  48 8B D1                        mov rdx, rcx
00471BF3  B8 01 00 00 00                  mov eax, 1
00471BF8  8A 0D 3A C0 9B 00               mov cl, byte ptr [rip + 0x9bc03a]
00471BFE  80 C1 F4                        add cl, 0xf4
00471C01  48 D3 E0                        shl rax, cl
00471C04  48 3B D0                        cmp rdx, rax
00471C07  73 05                           jae 0x140471c0e
00471C09  48 8B C2                        mov rax, rdx
00471C0C  C3                              ret
00471C0D  CC                              int3
00471C0E  48 FF C8                        dec rax
00471C11  48 23 D0                        and rdx, rax
00471C14  EB F3                           jmp 0x140471c09
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSanitizePage(__int64 a1)
{
    __int64 result;

    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 10207290)) + (244));
    result = (1) << ((unsigned __int8)(a1));
    if (a1 >= result) goto loc_00471C0E;
loc_00471C09:
    return a1;
loc_00471C0E:
    result = (a1) - 1;
    a2 = (a1) & (result);
    goto loc_00471C09;
}
```

## 5. (Beta) C Style

```c
int64_t MiSanitizePage(int64_t Arg1)
{
    int64_t result;

    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0x9BC03A)) + (244));
    result = (1) << ((uint8_t)(Arg1));
    if (Arg1 >= result) goto loc_00471C0E;
loc_00471C09:
    return Arg1;
loc_00471C0E:
    result = (Arg1) - 1;
    a2 = (Arg1) & (result);
    goto loc_00471C09;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00471BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00471BF0[BB_00471BF0]
  bb_00471C09[BB_00471C09]
  bb_00471C0D[BB_00471C0D]
  bb_00471C0E[BB_00471C0E]
  bb_00471BF0 -->|branch| bb_00471C0E
  bb_00471BF0 -->|fallthrough| bb_00471C09
  bb_00471C0D -->|flow| bb_00471C0E
  bb_00471C0E -->|branch| bb_00471C09
```
