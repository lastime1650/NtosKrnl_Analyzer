# FsRtlOplockBreakH2$fin$0

- RVA: `0x00B115DC`–`0x00B1160F` (길이 `51` bytes)
- VA: `0x0000000140B115DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AF154`
- 디코드: `13`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B115FF` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B115FF` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B115DC  40 55                           push rbp
00B115DE  48 81 EC 80 00 00 00            sub rsp, 0x80
00B115E5  48 8B EA                        mov rbp, rdx
00B115E8  80 BD D0 00 00 00 00            cmp byte ptr [rbp + 0xd0], 0
00B115EF  74 14                           je 0x140b11605
00B115F1  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
00B115F8  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
00B115FF  E8 9C ED 73 FF                  call 0x1402503a0
00B11604  90                              nop
00B11605  48 81 C4 80 00 00 00            add rsp, 0x80
00B1160C  5D                              pop rbp
00B1160D  C3                              ret
00B1160E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlOplockBreakH2_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (128);
    if ((*(unsigned __int8 *)(a2 + 208)) != 0) {
        a1 = *(unsigned __int64 *)(a2 + 136);
        a1 = *(unsigned __int64 *)(a1 + 152);
        result = ExReleaseFastMutexUnsafe(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlOplockBreakH2_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (128);
    if ((*(uint8_t *)(arg2 + 0xD0)) != 0) {
        Arg1 = *(uint64_t *)(arg2 + 0x88);
        Arg1 = *(uint64_t *)(Arg1 + 0x98);
        result = ExReleaseFastMutexUnsafe(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (128);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x88` | `64` | `R` |
| `Arg2` | `+ 0xD0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B115DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B115DC[BB_00B115DC]
  bb_00B115F1[BB_00B115F1]
  bb_00B11605[BB_00B11605]
  bb_00B1160E[BB_00B1160E]
  bb_00B115DC -->|branch| bb_00B11605
  bb_00B115DC -->|fallthrough| bb_00B115F1
  bb_00B115F1 -->|flow| bb_00B11605
```
