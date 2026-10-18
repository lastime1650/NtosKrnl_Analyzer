# RtlpAllocateHeap$fin$0

- RVA: `0x006D5B26`–`0x006D5B50` (길이 `42` bytes)
- VA: `0x00000001406D5B26`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000C766C`
- 디코드: `13`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D5B43` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D5B26  40 55                           push rbp
006D5B28  48 83 EC 40                     sub rsp, 0x40
006D5B2C  48 8B EA                        mov rbp, rdx
006D5B2F  80 7D 40 00                     cmp byte ptr [rbp + 0x40], 0
006D5B33  74 14                           je 0x1406d5b49
006D5B35  48 8B 8D 30 01 00 00            mov rcx, qword ptr [rbp + 0x130]
006D5B3C  48 8B 89 60 01 00 00            mov rcx, qword ptr [rcx + 0x160]
006D5B43  E8 C8 9E B8 FF                  call 0x14025fa10
006D5B48  90                              nop
006D5B49  48 83 C4 40                     add rsp, 0x40
006D5B4D  5D                              pop rbp
006D5B4E  C3                              ret
006D5B4F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpAllocateHeap_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    if ((*(unsigned __int8 *)(a2 + 64)) != 0) {
        a1 = *(unsigned __int64 *)(a2 + 304);
        a1 = *(unsigned __int64 *)(a1 + 352);
        result = ExReleaseResourceLite(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpAllocateHeap_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    if ((*(uint8_t *)(arg2 + 0x40)) != 0) {
        Arg1 = *(uint64_t *)(arg2 + 0x130);
        Arg1 = *(uint64_t *)(Arg1 + 0x160);
        result = ExReleaseResourceLite(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `8` | `R` |
| `Arg2` | `+ 0x130` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D5B26&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D5B26[BB_006D5B26]
  bb_006D5B35[BB_006D5B35]
  bb_006D5B49[BB_006D5B49]
  bb_006D5B4F[BB_006D5B4F]
  bb_006D5B26 -->|branch| bb_006D5B49
  bb_006D5B26 -->|fallthrough| bb_006D5B35
  bb_006D5B35 -->|flow| bb_006D5B49
```
