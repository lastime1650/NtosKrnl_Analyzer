# DebugService2

- RVA: `0x004FE530`–`0x004FE537` (길이 `7` bytes)
- VA: `0x00000001404FE530`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C244C`
- 디코드: `4`개 명령, `7/7` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DbgUnLoadImageSymbolsUnicode](../4A/DbgUnLoadImageSymbolsUnicode_function_004AE114.md) at `0x004AE161`
- [DbgLoadImageSymbols](../4A/DbgLoadImageSymbols_function_004AE220.md) at `0x004AE2A8`
- [DbgUnLoadImageSymbols](../4C/DbgUnLoadImageSymbols_function_004C6690.md) at `0x004C66B1`
- [DbgCommandString](../5E/DbgCommandString_function_005E56D0.md) at `0x005E5723`
- [DbgLoadUserImageSymbols](../5E/DbgLoadUserImageSymbols_function_005E57EC.md) at `0x005E5811`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FE530  41 8B C0                        mov eax, r8d
004FE533  CD 2D                           int 0x2d
004FE535  CC                              int3
004FE536  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DebugService2(__int64 a1, __int64 a2, int a3)
{
    return (unsigned int)(a3);
}
```

## 5. (Beta) C Style

```c
int64_t DebugService2(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    return (uint32_t)(Arg3);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FE530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FE530[BB_004FE530]
```
