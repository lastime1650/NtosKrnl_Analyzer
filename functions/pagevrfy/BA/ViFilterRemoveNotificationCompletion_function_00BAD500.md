# ViFilterRemoveNotificationCompletion

- RVA: `0x00BAD500`–`0x00BAD527` (길이 `39` bytes)
- VA: `0x0000000140BAD500`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAD517` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BAD517` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAD500  48 83 EC 28                     sub rsp, 0x28
00BAD504  80 7A 41 00                     cmp byte ptr [rdx + 0x41], 0
00BAD508  74 12                           je 0x140bad51c
00BAD50A  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00BAD50E  45 33 C0                        xor r8d, r8d
00BAD511  48 83 C1 40                     add rcx, 0x40
00BAD515  33 D2                           xor edx, edx
00BAD517  E8 F4 1D 79 FF                  call 0x14033f310
00BAD51C  B8 16 00 00 C0                  mov eax, 0xc0000016
00BAD521  48 83 C4 28                     add rsp, 0x28
00BAD525  C3                              ret
00BAD526  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViFilterRemoveNotificationCompletion(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(a2 + 65)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 64);
        a3 = 0;
        a1 = (a1) + (64);
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC0000016ULL);
}
```

## 5. (Beta) C Style

```c
int64_t ViFilterRemoveNotificationCompletion(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(arg2 + 0x41)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        Arg3 = 0;
        Arg1 = (Arg1) + (64);
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC0000016ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x41` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAD500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAD500[BB_00BAD500]
  bb_00BAD50A[BB_00BAD50A]
  bb_00BAD51C[BB_00BAD51C]
  bb_00BAD526[BB_00BAD526]
  bb_00BAD500 -->|branch| bb_00BAD51C
  bb_00BAD500 -->|fallthrough| bb_00BAD50A
  bb_00BAD50A -->|flow| bb_00BAD51C
```
