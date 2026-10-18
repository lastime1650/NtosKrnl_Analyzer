# PiEventAreDeviceRelationsExcluded

- RVA: `0x00A04EC0`–`0x00A04ED9` (길이 `25` bytes)
- VA: `0x0000000140A04EC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PnpProcessQueryRemoveAndEject](PnpProcessQueryRemoveAndEject_function_00A05170.md) at `0x00A0552B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A04EC0  83 F9 04                        cmp ecx, 4
00A04EC3  74 10                           je 0x140a04ed5
00A04EC5  B8 01 00 00 00                  mov eax, 1
00A04ECA  3B C8                           cmp ecx, eax
00A04ECC  7E 07                           jle 0x140a04ed5
00A04ECE  83 F9 07                        cmp ecx, 7
00A04ED1  7D 02                           jge 0x140a04ed5
00A04ED3  C3                              ret
00A04ED4  CC                              int3
00A04ED5  32 C0                           xor al, al
00A04ED7  C3                              ret
00A04ED8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiEventAreDeviceRelationsExcluded(int a1)
{
    __int64 result;

    if (a1 == 4) goto loc_00A04ED5;
    if (a1 <= 1) goto loc_00A04ED5;
    if (a1 >= 7) goto loc_00A04ED5;
    return 1;
loc_00A04ED5:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiEventAreDeviceRelationsExcluded(int32_t Arg1)
{
    int64_t result;

    if (Arg1 == 4) goto loc_00A04ED5;
    if (Arg1 <= 1) goto loc_00A04ED5;
    if (Arg1 >= 7) goto loc_00A04ED5;
    return 1;
loc_00A04ED5:
    result = 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A04EC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A04EC0[BB_00A04EC0]
  bb_00A04EC5[BB_00A04EC5]
  bb_00A04ECE[BB_00A04ECE]
  bb_00A04ED3[BB_00A04ED3]
  bb_00A04ED4[BB_00A04ED4]
  bb_00A04ED5[BB_00A04ED5]
  bb_00A04ED8[BB_00A04ED8]
  bb_00A04EC0 -->|branch| bb_00A04ED5
  bb_00A04EC0 -->|fallthrough| bb_00A04EC5
  bb_00A04EC5 -->|branch| bb_00A04ED5
  bb_00A04EC5 -->|fallthrough| bb_00A04ECE
  bb_00A04ECE -->|branch| bb_00A04ED5
  bb_00A04ECE -->|fallthrough| bb_00A04ED3
  bb_00A04ED4 -->|flow| bb_00A04ED5
```
