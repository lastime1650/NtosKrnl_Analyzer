# ViSpMmMapLockedPages_Entry

- RVA: `0x006AA9D0`–`0x006AA9E9` (길이 `25` bytes)
- VA: `0x00000001406AA9D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006AA9DE` → [ViSpMmMapLockedPagesSanityChecks](../../pagevrfy/BB/ViSpMmMapLockedPagesSanityChecks_function_00BB4B50.md) (function, `0x00BB4B50`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006AA9DE` → [ViSpMmMapLockedPagesSanityChecks](../../pagevrfy/BB/ViSpMmMapLockedPagesSanityChecks_function_00BB4B50.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AA9D0  48 83 EC 28                     sub rsp, 0x28
006AA9D4  4C 8B 01                        mov r8, qword ptr [rcx]
006AA9D7  8A 51 08                        mov dl, byte ptr [rcx + 8]
006AA9DA  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
006AA9DE  E8 6D A1 50 00                  call 0x140bb4b50
006AA9E3  48 83 C4 28                     add rsp, 0x28
006AA9E7  C3                              ret
006AA9E8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViSpMmMapLockedPages_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ViSpMmMapLockedPagesSanityChecks(*(unsigned __int64 *)(a1 + 16), *(unsigned __int8 *)(a1 + 8), *(unsigned __int64 *)(a1), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViSpMmMapLockedPages_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ViSpMmMapLockedPagesSanityChecks(*(uint64_t *)(arg1 + 0x10), *(uint8_t *)(arg1 + 0x8), *(uint64_t *)(arg1), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AA9D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AA9D0[BB_006AA9D0]
  bb_006AA9E8[BB_006AA9E8]
```
