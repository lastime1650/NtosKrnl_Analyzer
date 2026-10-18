# BgkpTryEnableConsole

- RVA: `0x005912D0`–`0x005912EC` (길이 `28` bytes)
- VA: `0x00000001405912D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [BgkNotifyDisplayOwnershipChange](BgkNotifyDisplayOwnershipChange_function_00590CC0.md) at `0x00590DAD`
- [BgkInitialize](../../init/C8/BgkInitialize_function_00C80488.md) at `0x00C8055D`

### Static image references
- `0x005912D2` → RVA `0x00E65EBA` (`.data`; read)
- `0x005912DA` → RVA `0x00E65E70` (`.data`; read)
- `0x005912E3` → RVA `0x00E0A9A0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005912D0  33 C0                           xor eax, eax
005912D2  38 05 E2 4B 8D 00               cmp byte ptr [rip + 0x8d4be2], al
005912D8  74 10                           je 0x1405912ea
005912DA  48 39 05 8F 4B 8D 00            cmp qword ptr [rip + 0x8d4b8f], rax
005912E1  74 07                           je 0x1405912ea
005912E3  48 87 05 B6 96 87 00            xchg qword ptr [rip + 0x8796b6], rax
005912EA  C3                              ret
005912EB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgkpTryEnableConsole(void)
{
    __int64 result;

    result = 0;
    if ((*(unsigned __int8 *)(v_rip + 9260002)) == 0) goto loc_005912EA;
    if ((*(unsigned __int64 *)(v_rip + 9259919)) != 0) {
    }
    return result;
}
```

## 5. (Beta) C Style

```c
void BgkpTryEnableConsole(void)
{
    int64_t result;

    result = 0;
    if ((*(uint8_t *)(v_rip + 0x8D4BE2)) == 0) goto loc_005912EA;
    if ((*(uint64_t *)(v_rip + 0x8D4B8F)) != 0) {
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005912D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005912D0[BB_005912D0]
  bb_005912DA[BB_005912DA]
  bb_005912E3[BB_005912E3]
  bb_005912EA[BB_005912EA]
  bb_005912EB[BB_005912EB]
  bb_005912D0 -->|branch| bb_005912EA
  bb_005912D0 -->|fallthrough| bb_005912DA
  bb_005912DA -->|branch| bb_005912EA
  bb_005912DA -->|fallthrough| bb_005912E3
  bb_005912E3 -->|flow| bb_005912EA
```
