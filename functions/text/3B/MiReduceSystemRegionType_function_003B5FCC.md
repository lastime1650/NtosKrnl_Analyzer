# MiReduceSystemRegionType

- RVA: `0x003B5FCC`–`0x003B5FE7` (길이 `27` bytes)
- VA: `0x00000001403B5FCC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiSplitBitmapPages](MiSplitBitmapPages_function_003B4A34.md) at `0x003B4A3E`
- [MiObtainDynamicVa](MiObtainDynamicVa_function_003B501C.md) at `0x003B5455`
- [MiMakeSystemRangeAvailable](../4E/MiMakeSystemRangeAvailable_function_004EE174.md) at `0x004EE349`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003B5FCC  83 F9 0C                        cmp ecx, 0xc
003B5FCF  75 09                           jne 0x1403b5fda
003B5FD1  B9 08 00 00 00                  mov ecx, 8
003B5FD6  8B C1                           mov eax, ecx
003B5FD8  C3                              ret
003B5FD9  CC                              int3
003B5FDA  83 F9 0A                        cmp ecx, 0xa
003B5FDD  B8 06 00 00 00                  mov eax, 6
003B5FE2  0F 44 C8                        cmove ecx, eax
003B5FE5  EB EF                           jmp 0x1403b5fd6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReduceSystemRegionType(int a1)
{
    if (a1 != 12) goto loc_003B5FDA;
loc_003B5FD6:
    return 8;
loc_003B5FDA:
    a1 = 8;
    if (8 == 10) { a1 = 6; }
    goto loc_003B5FD6;
}
```

## 5. (Beta) C Style

```c
int64_t MiReduceSystemRegionType(int32_t Arg1)
{
    if (Arg1 != 12) goto loc_003B5FDA;
loc_003B5FD6:
    return 8;
loc_003B5FDA:
    Arg1 = 8;
    if (8 == 10) { Arg1 = 6; }
    goto loc_003B5FD6;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B5FCC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003B5FCC[BB_003B5FCC]
  bb_003B5FD1[BB_003B5FD1]
  bb_003B5FD6[BB_003B5FD6]
  bb_003B5FD9[BB_003B5FD9]
  bb_003B5FDA[BB_003B5FDA]
  bb_003B5FCC -->|branch| bb_003B5FDA
  bb_003B5FCC -->|fallthrough| bb_003B5FD1
  bb_003B5FD1 -->|flow| bb_003B5FD6
  bb_003B5FD9 -->|flow| bb_003B5FDA
  bb_003B5FDA -->|branch| bb_003B5FD6
```
