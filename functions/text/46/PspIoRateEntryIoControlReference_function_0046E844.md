# PspIoRateEntryIoControlReference

- RVA: `0x0046E844`–`0x0046E86C` (길이 `40` bytes)
- VA: `0x000000014046E844`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CC84`
- 디코드: `15`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0046E851` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)

### Direct callers
- [PsIoRateControlReference](PsIoRateControlReference_function_0046E77C.md) at `0x0046E7AA`
- [PspJobIoRateVolumeEntryReference](../5E/PspJobIoRateVolumeEntryReference_function_005E3AA8.md) at `0x005E3B36`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046E844  40 53                           push rbx
0046E846  48 83 EC 20                     sub rsp, 0x20
0046E84A  48 8B D9                        mov rbx, rcx
0046E84D  48 83 C1 20                     add rcx, 0x20
0046E851  E8 CA 7D DA FF                  call 0x140216620
0046E856  33 D2                           xor edx, edx
0046E858  84 C0                           test al, al
0046E85A  75 0A                           jne 0x14046e866
0046E85C  48 8B C2                        mov rax, rdx
0046E85F  48 83 C4 20                     add rsp, 0x20
0046E863  5B                              pop rbx
0046E864  C3                              ret
0046E865  CC                              int3
0046E866  48 8B 53 28                     mov rdx, qword ptr [rbx + 0x28]
0046E86A  EB F0                           jmp 0x14046e85c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspIoRateEntryIoControlReference(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (32);
    result = ExAcquireRundownProtection(a1, a2, a3, a4);
    a2 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_0046E866;
loc_0046E85C:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_0046E866:
    goto loc_0046E85C;
}
```

## 5. (Beta) C Style

```c
int64_t PspIoRateEntryIoControlReference(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (32);
    result = ExAcquireRundownProtection(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    if ((uint8_t)(result) != 0) goto loc_0046E866;
loc_0046E85C:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_0046E866:
    goto loc_0046E85C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046E844&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046E844[BB_0046E844]
  bb_0046E85C[BB_0046E85C]
  bb_0046E865[BB_0046E865]
  bb_0046E866[BB_0046E866]
  bb_0046E844 -->|branch| bb_0046E866
  bb_0046E844 -->|fallthrough| bb_0046E85C
  bb_0046E865 -->|flow| bb_0046E866
  bb_0046E866 -->|branch| bb_0046E85C
```
