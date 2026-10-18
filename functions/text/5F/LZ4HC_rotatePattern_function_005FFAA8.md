# LZ4HC_rotatePattern

- RVA: `0x005FFAA8`–`0x005FFABA` (길이 `18` bytes)
- VA: `0x00000001405FFAA8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FAB52`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FABA0`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FB3CB`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FB41D`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FBD79`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FBDC6`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FD28F`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FD2DE`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FDD58`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FDDAA`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FE86D`
- [LZ4HC_compress_generic_dictCtx](LZ4HC_compress_generic_dictCtx_function_005F7D94.md) at `0x005FE8C3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005FFAA8  83 E1 03                        and ecx, 3
005FFAAB  48 C1 E1 03                     shl rcx, 3
005FFAAF  48 85 C9                        test rcx, rcx
005FFAB2  74 02                           je 0x1405ffab6
005FFAB4  D3 C2                           rol edx, cl
005FFAB6  8B C2                           mov eax, edx
005FFAB8  C3                              ret
005FFAB9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LZ4HC_rotatePattern(int a1, int a2)
{
    a1 = (unsigned int)((a1) & (3));
    a1 = (a1) << (3);
    if (a1 != 0) {
    }
    return (unsigned int)(a2);
}
```

## 5. (Beta) C Style

```c
int64_t LZ4HC_rotatePattern(int32_t Arg1, int32_t Arg2)
{
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg1 = (Arg1) << (3);
    if (Arg1 != 0) {
    }
    return (uint32_t)(Arg2);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005FFAA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005FFAA8[BB_005FFAA8]
  bb_005FFAB4[BB_005FFAB4]
  bb_005FFAB6[BB_005FFAB6]
  bb_005FFAB9[BB_005FFAB9]
  bb_005FFAA8 -->|branch| bb_005FFAB6
  bb_005FFAA8 -->|fallthrough| bb_005FFAB4
  bb_005FFAB4 -->|flow| bb_005FFAB6
```
