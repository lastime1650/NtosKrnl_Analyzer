# IommuInitializeLibrary

- RVA: `0x00565A64`–`0x00565A9B` (길이 `55` bytes)
- VA: `0x0000000140565A64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00565A8E` → [IommupHvInitializeLibrary](../../init/C2/IommupHvInitializeLibrary_function_00C25024.md) (function, `0x00C25024`)

### Direct callers
- [HalpIommuInitSystem](../../pagelk/B5/HalpIommuInitSystem_function_00B5D7E0.md) at `0x00B5D880`

### Static image references
- `0x00565A68` → RVA `0x00F8FB00` (`.data`; read/write)
- `0x00565A70` → RVA `0x00F8FB10` (`.data`; read)
- `0x00565A77` → RVA `0x00FC1710` (`.data`; read)
- `0x00565A7E` → RVA `0x00F8FB18` (`.data`; write)
- `0x00565A85` → RVA `0x00F8FB10` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00565A8E` → [IommupHvInitializeLibrary](../../init/C2/IommupHvInitializeLibrary_function_00C25024.md) (`.text` → `INIT`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00565A64  48 83 EC 28                     sub rsp, 0x28
00565A68  48 83 25 90 A0 A2 00 00         and qword ptr [rip + 0xa2a090], 0
00565A70  48 8D 05 99 A0 A2 00            lea rax, [rip + 0xa2a099]
00565A77  80 3D 92 BC A5 00 00            cmp byte ptr [rip + 0xa5bc92], 0
00565A7E  48 89 05 93 A0 A2 00            mov qword ptr [rip + 0xa2a093], rax
00565A85  48 89 05 84 A0 A2 00            mov qword ptr [rip + 0xa2a084], rax
00565A8C  74 05                           je 0x140565a93
00565A8E  E8 91 F5 6B 00                  call 0x140c25024
00565A93  33 C0                           xor eax, eax
00565A95  48 83 C4 28                     add rsp, 0x28
00565A99  C3                              ret
00565A9A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IommuInitializeLibrary(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(v_rip + 10657939) = v_rip + 10657945;
    *(unsigned __int64 *)(v_rip + 10657924) = v_rip + 10657945;
    result = v_rip + 10657945;
    if ((*(unsigned __int8 *)(v_rip + 10861714)) != 0) {
        result = IommupHvInitializeLibrary(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void IommuInitializeLibrary(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(v_rip + 0xA2A093) = v_rip + 10657945;
    *(uint64_t *)(v_rip + 0xA2A084) = v_rip + 10657945;
    result = v_rip + 10657945;
    if ((*(uint8_t *)(v_rip + 0xA5BC92)) != 0) {
        result = IommupHvInitializeLibrary(a1, a2, a3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00565A64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00565A64[BB_00565A64]
  bb_00565A8E[BB_00565A8E]
  bb_00565A93[BB_00565A93]
  bb_00565A9A[BB_00565A9A]
  bb_00565A64 -->|branch| bb_00565A93
  bb_00565A64 -->|fallthrough| bb_00565A8E
  bb_00565A8E -->|flow| bb_00565A93
```
