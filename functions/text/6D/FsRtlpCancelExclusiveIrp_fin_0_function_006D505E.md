# FsRtlpCancelExclusiveIrp$fin$0

- RVA: `0x006D505E`–`0x006D5085` (길이 `39` bytes)
- VA: `0x00000001406D505E`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `13`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D5078` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D505E  40 55                           push rbp
006D5060  48 83 EC 20                     sub rsp, 0x20
006D5064  48 8B EA                        mov rbp, rdx
006D5067  80 7D 38 00                     cmp byte ptr [rbp + 0x38], 0
006D506B  75 11                           jne 0x1406d507e
006D506D  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006D5071  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
006D5078  E8 43 C9 B7 FF                  call 0x1402519c0
006D507D  90                              nop
006D507E  48 83 C4 20                     add rsp, 0x20
006D5082  5D                              pop rbp
006D5083  C3                              ret
006D5084  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpCancelExclusiveIrp_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int8 *)(a2 + 56)) == 0) {
        a1 = *(unsigned __int64 *)(a2 + 48);
        a1 = *(unsigned __int64 *)(a1 + 152);
        result = ExReleaseFastMutex(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpCancelExclusiveIrp_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint8_t *)(arg2 + 0x38)) == 0) {
        Arg1 = *(uint64_t *)(arg2 + 0x30);
        Arg1 = *(uint64_t *)(Arg1 + 0x98);
        result = ExReleaseFastMutex(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x38` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D505E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D505E[BB_006D505E]
  bb_006D506D[BB_006D506D]
  bb_006D507E[BB_006D507E]
  bb_006D5084[BB_006D5084]
  bb_006D505E -->|branch| bb_006D507E
  bb_006D505E -->|fallthrough| bb_006D506D
  bb_006D506D -->|flow| bb_006D507E
```
