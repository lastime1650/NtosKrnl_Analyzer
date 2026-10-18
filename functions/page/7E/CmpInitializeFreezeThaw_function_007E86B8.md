# CmpInitializeFreezeThaw

- RVA: `0x007E86B8`–`0x007E86ED` (길이 `53` bytes)
- VA: `0x00000001407E86B8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmInitSystem1](../../init/C5/CmInitSystem1_function_00C559CC.md) at `0x00C55C54`

### Static image references
- `0x007E86B8` → RVA `0x00EF71C0` (`.data`; read/write)
- `0x007E86C0` → RVA `0x00EF71D0` (`.data`; read)
- `0x007E86C7` → RVA `0x00E0EC90` (`.data`; read)
- `0x007E86D1` → RVA `0x00EF71D8` (`.data`; write)
- `0x007E86D8` → RVA `0x00EF71D0` (`.data`; write)
- `0x007E86E1` → RVA `0x00E0EC90` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E86B8  48 83 25 00 EB 70 00 00         and qword ptr [rip + 0x70eb00], 0
007E86C0  48 8D 05 09 EB 70 00            lea rax, [rip + 0x70eb09]
007E86C7  81 3D BF 65 62 00 84 03 00 00   cmp dword ptr [rip + 0x6265bf], 0x384
007E86D1  48 89 05 00 EB 70 00            mov qword ptr [rip + 0x70eb00], rax
007E86D8  48 89 05 F1 EA 70 00            mov qword ptr [rip + 0x70eaf1], rax
007E86DF  76 0A                           jbe 0x1407e86eb
007E86E1  C7 05 A5 65 62 00 3C 00 00 00   mov dword ptr [rip + 0x6265a5], 0x3c
007E86EB  C3                              ret
007E86EC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpInitializeFreezeThaw(void)
{
    *(unsigned __int64 *)(v_rip + 7400192) = v_rip + 7400201;
    *(unsigned __int64 *)(v_rip + 7400177) = v_rip + 7400201;
    if ((*(unsigned int *)(v_rip + 6448575)) >= = 900) {
        *(unsigned int *)(v_rip + 6448549) = 60;
    }
    return v_rip + 7400201;
}
```

## 5. (Beta) C Style

```c
void CmpInitializeFreezeThaw(void)
{
    *(uint64_t *)(v_rip + 0x70EB00) = v_rip + 7400201;
    *(uint64_t *)(v_rip + 0x70EAF1) = v_rip + 7400201;
    if ((*(uint32_t *)(v_rip + 0x6265BF)) >= = 900) {
        *(uint32_t *)(v_rip + 0x6265A5) = 60;
    }
    return v_rip + 7400201;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E86B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E86B8[BB_007E86B8]
  bb_007E86E1[BB_007E86E1]
  bb_007E86EB[BB_007E86EB]
  bb_007E86EC[BB_007E86EC]
  bb_007E86B8 -->|branch| bb_007E86EB
  bb_007E86B8 -->|fallthrough| bb_007E86E1
  bb_007E86E1 -->|flow| bb_007E86EB
```
