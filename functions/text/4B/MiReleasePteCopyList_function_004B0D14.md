# MiReleasePteCopyList

- RVA: `0x004B0D14`–`0x004B0D37` (길이 `35` bytes)
- VA: `0x00000001404B0D14`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B0D2C` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)

### Direct callers
- [MiCopyPagesIntoEnclave](../../page/A4/MiCopyPagesIntoEnclave_function_00A472AC.md) at `0x00A47680`

### Static image references
- `0x004B0D25` → RVA `0x00E37668` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B0D14  48 83 EC 28                     sub rsp, 0x28
004B0D18  44 8B 41 04                     mov r8d, dword ptr [rcx + 4]
004B0D1C  45 85 C0                        test r8d, r8d
004B0D1F  74 10                           je 0x1404b0d31
004B0D21  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
004B0D25  48 8D 0D 3C 69 98 00            lea rcx, [rip + 0x98693c]
004B0D2C  E8 0F 65 D9 FF                  call 0x140247240
004B0D31  48 83 C4 28                     add rsp, 0x28
004B0D35  C3                              ret
004B0D36  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleasePteCopyList(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 16);
        a1 = v_rip + 9988412;
        result = MiReleasePtes(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 4)), a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleasePteCopyList(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) != 0) {
        a2 = *(uint64_t *)(arg1 + 0x10);
        Arg1 = v_rip + 9988412;
        result = MiReleasePtes(Arg1, a2, (uint32_t)(*(uint32_t *)(arg1 + 0x4)), a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B0D14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B0D14[BB_004B0D14]
  bb_004B0D21[BB_004B0D21]
  bb_004B0D31[BB_004B0D31]
  bb_004B0D36[BB_004B0D36]
  bb_004B0D14 -->|branch| bb_004B0D31
  bb_004B0D14 -->|fallthrough| bb_004B0D21
  bb_004B0D21 -->|flow| bb_004B0D31
```
