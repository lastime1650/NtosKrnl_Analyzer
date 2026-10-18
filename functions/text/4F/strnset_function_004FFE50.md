# strnset

- RVA: `0x004FFE50`–`0x004FFE69` (길이 `25` bytes)
- VA: `0x00000001404FFE50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FFE50  48 8B C1                        mov rax, rcx
004FFE53  EB 0D                           jmp 0x1404ffe62
004FFE55  49 FF C8                        dec r8
004FFE58  80 39 00                        cmp byte ptr [rcx], 0
004FFE5B  74 0A                           je 0x1404ffe67
004FFE5D  88 11                           mov byte ptr [rcx], dl
004FFE5F  48 FF C1                        inc rcx
004FFE62  4D 85 C0                        test r8, r8
004FFE65  75 EE                           jne 0x1404ffe55
004FFE67  C3                              ret
004FFE68  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall strnset(__int64 a1, unsigned __int8 a2, __int64 a3)
{
    goto loc_004FFE62;
loc_004FFE55:
    a3 = (a3) - 1;
    if ((*(unsigned __int8 *)(a1)) == 0) goto loc_004FFE67;
    *(unsigned __int8 *)(a1) = a2;
    a1 = (a1) + 1;
loc_004FFE62:
    if (a3 != 0) goto loc_004FFE55;
loc_004FFE67:
    return a1;
}
```

## 5. (Beta) C Style

```c
int64_t strnset(int64_t Arg1, uint8_t Arg2, int64_t Arg3)
{
    goto loc_004FFE62;
loc_004FFE55:
    Arg3 = (Arg3) - 1;
    if ((*(uint8_t *)(Arg1)) == 0) goto loc_004FFE67;
    *(uint8_t *)(Arg1) = Arg2;
    Arg1 = (Arg1) + 1;
loc_004FFE62:
    if (Arg3 != 0) goto loc_004FFE55;
loc_004FFE67:
    return Arg1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FFE50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FFE50[BB_004FFE50]
  bb_004FFE55[BB_004FFE55]
  bb_004FFE5D[BB_004FFE5D]
  bb_004FFE62[BB_004FFE62]
  bb_004FFE67[BB_004FFE67]
  bb_004FFE68[BB_004FFE68]
  bb_004FFE50 -->|branch| bb_004FFE62
  bb_004FFE55 -->|branch| bb_004FFE67
  bb_004FFE55 -->|fallthrough| bb_004FFE5D
  bb_004FFE5D -->|flow| bb_004FFE62
  bb_004FFE62 -->|branch| bb_004FFE55
  bb_004FFE62 -->|fallthrough| bb_004FFE67
```
