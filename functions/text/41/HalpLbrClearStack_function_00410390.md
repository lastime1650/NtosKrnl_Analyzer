# HalpLbrClearStack

- RVA: `0x00410390`–`0x004103AE` (길이 `30` bytes)
- VA: `0x0000000140410390`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BC54`
- 디코드: `9`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00410394` → RVA `0x00F8F998` (`.data`; read)
- `0x004103A5` → RVA `0x00F8F99C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00410390  48 83 EC 28                     sub rsp, 0x28
00410394  83 3D FD F5 B7 00 00            cmp dword ptr [rip + 0xb7f5fd], 0
0041039B  75 08                           jne 0x1404103a5
0041039D  32 C0                           xor al, al
0041039F  48 83 C4 28                     add rsp, 0x28
004103A3  C3                              ret
004103A4  CC                              int3
004103A5  83 3D F0 F5 B7 00 00            cmp dword ptr [rip + 0xb7f5f0], 0
004103AC  74 EF                           je 0x14041039d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpLbrClearStack(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 12056061)) != 0) goto loc_004103A5;
loc_0041039D:
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
loc_004103A5:
    if ((*(unsigned int *)(v_rip + 12056048)) == 0) goto loc_0041039D;
}
```

## 5. (Beta) C Style

```c
void HalpLbrClearStack(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0xB7F5FD)) != 0) goto loc_004103A5;
loc_0041039D:
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
loc_004103A5:
    if ((*(uint32_t *)(v_rip + 0xB7F5F0)) == 0) goto loc_0041039D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00410390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00410390[BB_00410390]
  bb_0041039D[BB_0041039D]
  bb_004103A4[BB_004103A4]
  bb_004103A5[BB_004103A5]
  bb_00410390 -->|branch| bb_004103A5
  bb_00410390 -->|fallthrough| bb_0041039D
  bb_004103A4 -->|flow| bb_004103A5
  bb_004103A5 -->|branch| bb_0041039D
```
