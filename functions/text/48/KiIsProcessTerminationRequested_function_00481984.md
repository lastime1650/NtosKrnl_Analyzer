# KiIsProcessTerminationRequested

- RVA: `0x00481984`–`0x004819D9` (길이 `85` bytes)
- VA: `0x0000000140481984`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AECE4`
- 디코드: `21`개 명령, `85/85` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004819C0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiSchedulerApcTerminate](../../page/90/KiSchedulerApcTerminate_function_00905D40.md) at `0x00905D57`

### Static image references
- `0x00481988` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00481984  48 83 EC 28                     sub rsp, 0x28
00481988  48 8B 05 B1 8D 98 00            mov rax, qword ptr [rip + 0x988db1]
0048198F  48 33 C4                        xor rax, rsp
00481992  48 89 44 24 10                  mov qword ptr [rsp + 0x10], rax
00481997  8B 41 78                        mov eax, dword ptr [rcx + 0x78]
0048199A  C7 04 24 2D 01 00 C0            mov dword ptr [rsp], 0xc000012d
004819A1  C7 44 24 04 24 07 00 C0         mov dword ptr [rsp + 4], 0xc0000724
004819A9  C7 44 24 08 25 07 00 C0         mov dword ptr [rsp + 8], 0xc0000725
004819B1  25 00 00 0C 00                  and eax, 0xc0000
004819B6  75 13                           jne 0x1404819cb
004819B8  48 8B 4C 24 10                  mov rcx, qword ptr [rsp + 0x10]
004819BD  48 33 CC                        xor rcx, rsp
004819C0  E8 7B AC 22 00                  call 0x1406ac640
004819C5  48 83 C4 28                     add rsp, 0x28
004819C9  C3                              ret
004819CA  CC                              int3
004819CB  48 C1 E8 12                     shr rax, 0x12
004819CF  8B 44 84 FC                     mov eax, dword ptr [rsp + rax*4 - 4]
004819D3  89 02                           mov dword ptr [rdx], eax
004819D5  B0 01                           mov al, 1
004819D7  EB DF                           jmp 0x1404819b8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiIsProcessTerminationRequested(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (40);
    result = (*(unsigned __int64 *)(v_rip + 9997745)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = 0xC000012DULL;
    v_stack_m24 = 0xC0000724ULL;
    v_stack_m20 = 0xC0000725ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 120))) & (0xC0000ULL));
    if (condition_is_not_equal) goto loc_004819CB;
loc_004819B8:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_004819CB:
    result = (result) >> (18);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 4 - 4)));
    goto loc_004819B8;
}
```

## 5. (Beta) C Style

```c
int64_t KiIsProcessTerminationRequested(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (40);
    result = (*(uint64_t *)(v_rip + 0x988DB1)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = 0xC000012DULL;
    v_stack_m24 = 0xC0000724ULL;
    v_stack_m20 = 0xC0000725ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x78))) & (0xC0000ULL));
    if (condition_is_not_equal) goto loc_004819CB;
loc_004819B8:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_004819CB:
    result = (result) >> (18);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 4 - 0x4)));
    goto loc_004819B8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00481984&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00481984[BB_00481984]
  bb_004819B8[BB_004819B8]
  bb_004819CA[BB_004819CA]
  bb_004819CB[BB_004819CB]
  bb_00481984 -->|branch| bb_004819CB
  bb_00481984 -->|fallthrough| bb_004819B8
  bb_004819CA -->|flow| bb_004819CB
  bb_004819CB -->|branch| bb_004819B8
```
