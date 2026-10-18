# PsGetJobServerSilo

- RVA: `0x004C2440`–`0x004C2469` (길이 `41` bytes)
- VA: `0x00000001404C2440`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE6C`
- 디코드: `15`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004C245D` → [PsGetEffectiveServerSilo](../22/PsGetEffectiveServerSilo_function_002257F0.md) (function, `0x002257F0`)

### Direct callers
- [NtQueryInformationJobObject](../../page/9F/NtQueryInformationJobObject_function_009FB860.md) at `0x009FC625`
- [sub_00B316B4](../../page/B3/Unknown_function_00B316B4.md) at `0x00B31EF4`
- [sub_00B316B4](../../page/B3/Unknown_function_00B316B4.md) at `0x00B323E5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C2440  40 53                           push rbx
004C2442  48 83 EC 20                     sub rsp, 0x20
004C2446  48 8B DA                        mov rbx, rdx
004C2449  48 85 C9                        test rcx, rcx
004C244C  75 0F                           jne 0x1404c245d
004C244E  48 21 0A                        and qword ptr [rdx], rcx
004C2451  B8 0D 00 00 C0                  mov eax, 0xc000000d
004C2456  48 83 C4 20                     add rsp, 0x20
004C245A  5B                              pop rbx
004C245B  C3                              ret
004C245C  CC                              int3
004C245D  E8 8E 33 D6 FF                  call 0x1402257f0
004C2462  48 89 03                        mov qword ptr [rbx], rax
004C2465  33 C0                           xor eax, eax
004C2467  EB ED                           jmp 0x1404c2456
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetJobServerSilo(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a1 != 0) goto loc_004C245D;
loc_004C2456:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(0xC000000DULL);
loc_004C245D:
    result = PsGetEffectiveServerSilo(a1, a2, a3, a4);
    *(unsigned __int64 *)(a2) = result;
    result = 0;
    goto loc_004C2456;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetJobServerSilo(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg1 != 0) goto loc_004C245D;
loc_004C2456:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(0xC000000DULL);
loc_004C245D:
    result = PsGetEffectiveServerSilo(Arg1, Arg2, a3, a4);
    *(uint64_t *)(arg2) = result;
    result = 0;
    goto loc_004C2456;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C2440&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C2440[BB_004C2440]
  bb_004C244E[BB_004C244E]
  bb_004C2456[BB_004C2456]
  bb_004C245C[BB_004C245C]
  bb_004C245D[BB_004C245D]
  bb_004C2440 -->|branch| bb_004C245D
  bb_004C2440 -->|fallthrough| bb_004C244E
  bb_004C244E -->|flow| bb_004C2456
  bb_004C245C -->|flow| bb_004C245D
  bb_004C245D -->|branch| bb_004C2456
```
