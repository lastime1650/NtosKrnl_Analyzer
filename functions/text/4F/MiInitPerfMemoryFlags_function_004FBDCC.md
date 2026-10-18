# MiInitPerfMemoryFlags

- RVA: `0x004FBDCC`–`0x004FBDDC` (길이 `16` bytes)
- VA: `0x00000001404FBDCC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiLogSectionCreate](../../page/7F/MiLogSectionCreate_function_007FCDEC.md) at `0x007FCEA7`
- [sub_00B190F2](../../page/B1/Unknown_function_00B190F2.md) at `0x00B1916D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FBDCC  33 C0                           xor eax, eax
004FBDCE  85 C9                           test ecx, ecx
004FBDD0  0F 95 C0                        setne al
004FBDD3  83 E2 0F                        and edx, 0xf
004FBDD6  03 D2                           add edx, edx
004FBDD8  0B C2                           or eax, edx
004FBDDA  C3                              ret
004FBDDB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitPerfMemoryFlags(int a1, int a2)
{
    __int64 result;

    result = 0;
    result = (a1 != 0) ? 1 : 0;
    a2 = (unsigned int)((a2) & (15));
    a2 = (unsigned int)((a2) + (a2));
    result = (unsigned int)((result) | (a2));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitPerfMemoryFlags(int32_t Arg1, int32_t Arg2)
{
    int64_t result;

    result = 0;
    result = (Arg1 != 0) ? 1 : 0;
    Arg2 = (uint32_t)((Arg2) & (15));
    Arg2 = (uint32_t)((Arg2) + (Arg2));
    result = (uint32_t)((result) | (Arg2));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FBDCC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FBDCC[BB_004FBDCC]
  bb_004FBDDB[BB_004FBDDB]
```
