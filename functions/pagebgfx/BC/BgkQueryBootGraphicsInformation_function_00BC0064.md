# BgkQueryBootGraphicsInformation

- RVA: `0x00BC0064`–`0x00BC0083` (길이 `31` bytes)
- VA: `0x0000000140BC0064`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BC0078` → [BgQueryBootGraphicsInformation](../../text/69/BgQueryBootGraphicsInformation_function_0069EA44.md) (function, `0x0069EA44`)

### Direct callers
- [ExpQuerySystemInformation](../../page/A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A59B73`
- [ExpQuerySystemInformation](../../page/A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A59EF7`
- [ExpQuerySystemInformation](../../page/A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A59F28`
- [ExpQuerySystemInformation](../../page/A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5A21C`

### Static image references
- `0x00BC0068` → RVA `0x00E65EB0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BC0078` → [BgQueryBootGraphicsInformation](../../text/69/BgQueryBootGraphicsInformation_function_0069EA44.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC0064  48 83 EC 28                     sub rsp, 0x28
00BC0068  80 3D 41 5E 2A 00 00            cmp byte ptr [rip + 0x2a5e41], 0
00BC006F  75 07                           jne 0x140bc0078
00BC0071  B8 01 00 00 C0                  mov eax, 0xc0000001
00BC0076  EB 05                           jmp 0x140bc007d
00BC0078  E8 C7 E9 AD FF                  call 0x14069ea44
00BC007D  48 83 C4 28                     add rsp, 0x28
00BC0081  C3                              ret
00BC0082  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgkQueryBootGraphicsInformation(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 2776641)) != 0) goto loc_00BC0078;
    goto loc_00BC007D;
loc_00BC0078:
    result = BgQueryBootGraphicsInformation(a1, a2, a3, a4);
loc_00BC007D:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void BgkQueryBootGraphicsInformation(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0x2A5E41)) != 0) goto loc_00BC0078;
    goto loc_00BC007D;
loc_00BC0078:
    result = BgQueryBootGraphicsInformation(a1, a2, a3, a4);
loc_00BC007D:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC0064&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC0064[BB_00BC0064]
  bb_00BC0071[BB_00BC0071]
  bb_00BC0078[BB_00BC0078]
  bb_00BC007D[BB_00BC007D]
  bb_00BC0082[BB_00BC0082]
  bb_00BC0064 -->|branch| bb_00BC0078
  bb_00BC0064 -->|fallthrough| bb_00BC0071
  bb_00BC0071 -->|branch| bb_00BC007D
  bb_00BC0078 -->|flow| bb_00BC007D
```
