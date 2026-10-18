# KiRcuStartGracePeriodEnumCallback

- RVA: `0x004D0C48`–`0x004D0C82` (길이 `58` bytes)
- VA: `0x00000001404D0C48`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004D0C67` → [KiRcuCheckQuiescentForIdle](KiRcuCheckQuiescentForIdle_function_004DF6FC.md) (function, `0x004DF6FC`)

### Direct callers
- [KiRcuForEachParticipatingCpu](KiRcuForEachParticipatingCpu_function_004D0FE4.md) at `0x004D1051`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D0C48  40 53                           push rbx
004D0C4A  48 83 EC 20                     sub rsp, 0x20
004D0C4E  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
004D0C52  48 8B DA                        mov rbx, rdx
004D0C55  41 80 B8 E7 38 00 00 00         cmp byte ptr [r8 + 0x38e7], 0
004D0C5D  41 C6 80 E5 38 00 00 01         mov byte ptr [r8 + 0x38e5], 1
004D0C65  75 0F                           jne 0x1404d0c76
004D0C67  E8 90 EA 00 00                  call 0x1404df6fc
004D0C6C  85 C0                           test eax, eax
004D0C6E  74 06                           je 0x1404d0c76
004D0C70  C7 03 01 00 00 00               mov dword ptr [rbx], 1
004D0C76  B8 01 00 00 00                  mov eax, 1
004D0C7B  48 83 C4 20                     add rsp, 0x20
004D0C7F  5B                              pop rbx
004D0C80  C3                              ret
004D0C81  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiRcuStartGracePeriodEnumCallback(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 16) + 14565) = 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 16) + 14567)) != 0) goto loc_004D0C76;
    result = KiRcuCheckQuiescentForIdle(a1, a2, *(unsigned __int64 *)(a1 + 16), a4);
    if ((unsigned int)(result) != 0) {
        *(unsigned int *)(a2) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t KiRcuStartGracePeriodEnumCallback(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38E5) = 1;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x10) + 0x38E7)) != 0) goto loc_004D0C76;
    result = KiRcuCheckQuiescentForIdle(Arg1, Arg2, *(uint64_t *)(arg1 + 0x10), a4);
    if ((uint32_t)(result) != 0) {
        *(uint32_t *)(arg2) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D0C48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D0C48[BB_004D0C48]
  bb_004D0C67[BB_004D0C67]
  bb_004D0C70[BB_004D0C70]
  bb_004D0C76[BB_004D0C76]
  bb_004D0C81[BB_004D0C81]
  bb_004D0C48 -->|branch| bb_004D0C76
  bb_004D0C48 -->|fallthrough| bb_004D0C67
  bb_004D0C67 -->|branch| bb_004D0C76
  bb_004D0C67 -->|fallthrough| bb_004D0C70
  bb_004D0C70 -->|flow| bb_004D0C76
```
