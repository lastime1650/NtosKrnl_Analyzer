# FsRtlLookupLastBaseMcbEntry

- RVA: `0x004481C0`–`0x004481D8` (길이 `24` bytes)
- VA: `0x00000001404481C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A601C`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [FsRtlLookupLastLargeMcbEntry](../58/FsRtlLookupLastLargeMcbEntry_function_00581250.md) at `0x00581280`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x004481CE` → [sub_00448224 + 0x6](Unknown_function_00448224.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
004481C0  48 83 EC 08                     sub rsp, 8
004481C4  44 8B 49 04                     mov r9d, dword ptr [rcx + 4]
004481C8  4C 8B D2                        mov r10, rdx
004481CB  45 85 C9                        test r9d, r9d
004481CE  74 5A                           je 0x14044822a
004481D0  4C 8B 59 10                     mov r11, qword ptr [rcx + 0x10]
004481D4  41 8D 51 FF                     lea edx, [r9 - 1]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall FsRtlLookupLastBaseMcbEntry(__int64 a1, __int64 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (8);
    return;
}
```

## 5. (Beta) C Style

```c
void FsRtlLookupLastBaseMcbEntry(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (8);
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004481C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004481C0[BB_004481C0]
  bb_004481D0[BB_004481D0]
  bb_004481C0 -->|fallthrough| bb_004481D0
```
