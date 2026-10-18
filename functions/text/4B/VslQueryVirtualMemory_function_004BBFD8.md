# VslQueryVirtualMemory

- RVA: `0x004BBFD8`–`0x004BC06F` (길이 `151` bytes)
- VA: `0x00000001404BBFD8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB820`
- 디코드: `40`개 명령, `151/151` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004BC009` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004BC02E` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x004BC042` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MmQueryVirtualMemory](../../page/9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D982A`

### Static image references
- `0x004BBFE3` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BBFD8  40 53                           push rbx
004BBFDA  56                              push rsi
004BBFDB  57                              push rdi
004BBFDC  48 81 EC A0 00 00 00            sub rsp, 0xa0
004BBFE3  48 8B 05 56 E7 94 00            mov rax, qword ptr [rip + 0x94e756]
004BBFEA  48 33 C4                        xor rax, rsp
004BBFED  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
004BBFF5  48 8B FA                        mov rdi, rdx
004BBFF8  49 8B F0                        mov rsi, r8
004BBFFB  33 D2                           xor edx, edx
004BBFFD  48 8B D9                        mov rbx, rcx
004BC000  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
004BC005  44 8D 42 68                     lea r8d, [rdx + 0x68]
004BC009  E8 32 AC 20 00                  call 0x1406c6c40
004BC00E  48 8B 83 70 01 00 00            mov rax, qword ptr [rbx + 0x170]
004BC015  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
004BC01A  BA 2A 00 00 00                  mov edx, 0x2a
004BC01F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004BC024  45 33 C0                        xor r8d, r8d
004BC027  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
004BC02C  B1 02                           mov cl, 2
004BC02E  E8 1D 9E D7 FF                  call 0x140235e50
004BC033  85 C0                           test eax, eax
004BC035  79 1C                           jns 0x1404bc053
004BC037  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
004BC03F  48 33 CC                        xor rcx, rsp
004BC042  E8 F9 05 1F 00                  call 0x1406ac640
004BC047  48 81 C4 A0 00 00 00            add rsp, 0xa0
004BC04E  5F                              pop rdi
004BC04F  5E                              pop rsi
004BC050  5B                              pop rbx
004BC051  C3                              ret
004BC052  CC                              int3
004BC053  0F 28 44 24 30                  movaps xmm0, xmmword ptr [rsp + 0x30]
004BC058  0F 28 4C 24 40                  movaps xmm1, xmmword ptr [rsp + 0x40]
004BC05D  0F 11 06                        movups xmmword ptr [rsi], xmm0
004BC060  0F 28 44 24 50                  movaps xmm0, xmmword ptr [rsp + 0x50]
004BC065  0F 11 4E 10                     movups xmmword ptr [rsi + 0x10], xmm1
004BC069  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
004BC06D  EB C8                           jmp 0x1404bc037
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslQueryVirtualMemory(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 9758550)) ^ (v_rsp);
    v_stack_m28 = result;
    a2 = 0;
    result = memset(v_stack_m98, a2, a2 + 104, a4);
    v_stack_m90 = *(unsigned __int64 *)(a1 + 368);
    a3 = 0;
    v_stack_m88 = 0;
    result = VslpEnterIumSecureMode(2, 42, a3, v_stack_m98);
    if (!sign_flag) goto loc_004BC053;
loc_004BC037:
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, 42, a3, v_stack_m98);
    v_rsp = (v_rsp) + (160);
    return result;
loc_004BC053:
    *(unsigned __int64 *)(a3) = v_xmm0;
    *(unsigned __int64 *)(a3 + 16) = v_xmm1;
    *(unsigned __int64 *)(a3 + 32) = v_xmm0;
    goto loc_004BC037;
}
```

## 5. (Beta) C Style

```c
int64_t VslQueryVirtualMemory(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x94E756)) ^ (local_rsp);
    v_stack_m28 = result;
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, Arg2 + 104, a4);
    v_stack_m90 = *(uint64_t *)(arg1 + 0x170);
    Arg3 = 0;
    v_stack_m88 = 0;
    result = VslpEnterIumSecureMode(2, 42, Arg3, v_stack_m98);
    if (!sign_flag) goto loc_004BC053;
loc_004BC037:
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 42, Arg3, v_stack_m98);
    local_rsp = (local_rsp) + (160);
    return result;
loc_004BC053:
    *(uint64_t *)(arg3) = v_xmm0;
    *(uint64_t *)(arg3 + 0x10) = v_xmm1;
    *(uint64_t *)(arg3 + 0x20) = v_xmm0;
    goto loc_004BC037;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x170` | `64` | `R` |
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x10` | `128` | `R` |
| `Arg3` | `+ 0x20` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BBFD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BBFD8[BB_004BBFD8]
  bb_004BC037[BB_004BC037]
  bb_004BC052[BB_004BC052]
  bb_004BC053[BB_004BC053]
  bb_004BBFD8 -->|branch| bb_004BC053
  bb_004BBFD8 -->|fallthrough| bb_004BC037
  bb_004BC052 -->|flow| bb_004BC053
  bb_004BC053 -->|branch| bb_004BC037
```
