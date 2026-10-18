# VslpKsrEnterIumSecureMode

- RVA: `0x0058FB90`–`0x0058FC51` (길이 `193` bytes)
- VA: `0x000000014058FB90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C6AD4`
- 디코드: `49`개 명령, `193/193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0058FBBD` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0058FBFF` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x0058FC3A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0058FBA2` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058FB90  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0058FB95  55                              push rbp
0058FB96  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0058FB9B  48 81 EC A0 00 00 00            sub rsp, 0xa0
0058FBA2  48 8B 05 97 AB 87 00            mov rax, qword ptr [rip + 0x87ab97]
0058FBA9  48 33 C4                        xor rax, rsp
0058FBAC  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0058FBB0  33 D2                           xor edx, edx
0058FBB2  48 8B D9                        mov rbx, rcx
0058FBB5  48 8D 4D D7                     lea rcx, [rbp - 0x29]
0058FBB9  44 8D 42 68                     lea r8d, [rdx + 0x68]
0058FBBD  E8 7E 70 13 00                  call 0x1406c6c40
0058FBC2  0F 10 03                        movups xmm0, xmmword ptr [rbx]
0058FBC5  BA 10 01 00 00                  mov edx, 0x110
0058FBCA  4C 8D 4D D7                     lea r9, [rbp - 0x29]
0058FBCE  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
0058FBD2  45 33 C0                        xor r8d, r8d
0058FBD5  B1 02                           mov cl, 2
0058FBD7  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
0058FBDB  0F 10 43 20                     movups xmm0, xmmword ptr [rbx + 0x20]
0058FBDF  0F 11 4D EF                     movups xmmword ptr [rbp - 0x11], xmm1
0058FBE3  0F 10 4B 30                     movups xmm1, xmmword ptr [rbx + 0x30]
0058FBE7  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
0058FBEB  0F 10 43 40                     movups xmm0, xmmword ptr [rbx + 0x40]
0058FBEF  0F 11 4D 0F                     movups xmmword ptr [rbp + 0xf], xmm1
0058FBF3  0F 10 4B 50                     movups xmm1, xmmword ptr [rbx + 0x50]
0058FBF7  0F 11 45 1F                     movups xmmword ptr [rbp + 0x1f], xmm0
0058FBFB  0F 11 4D 2F                     movups xmmword ptr [rbp + 0x2f], xmm1
0058FBFF  E8 4C 62 CA FF                  call 0x140235e50
0058FC04  0F 10 45 DF                     movups xmm0, xmmword ptr [rbp - 0x21]
0058FC08  0F 10 4D EF                     movups xmm1, xmmword ptr [rbp - 0x11]
0058FC0C  0F 11 03                        movups xmmword ptr [rbx], xmm0
0058FC0F  0F 10 45 FF                     movups xmm0, xmmword ptr [rbp - 1]
0058FC13  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
0058FC17  0F 10 4D 0F                     movups xmm1, xmmword ptr [rbp + 0xf]
0058FC1B  0F 11 43 20                     movups xmmword ptr [rbx + 0x20], xmm0
0058FC1F  0F 10 45 1F                     movups xmm0, xmmword ptr [rbp + 0x1f]
0058FC23  0F 11 4B 30                     movups xmmword ptr [rbx + 0x30], xmm1
0058FC27  0F 10 4D 2F                     movups xmm1, xmmword ptr [rbp + 0x2f]
0058FC2B  0F 11 43 40                     movups xmmword ptr [rbx + 0x40], xmm0
0058FC2F  0F 11 4B 50                     movups xmmword ptr [rbx + 0x50], xmm1
0058FC33  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0058FC37  48 33 CC                        xor rcx, rsp
0058FC3A  E8 01 CA 11 00                  call 0x1406ac640
0058FC3F  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
0058FC47  48 81 C4 A0 00 00 00            add rsp, 0xa0
0058FC4E  5D                              pop rbp
0058FC4F  C3                              ret
0058FC50  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslpKsrEnterIumSecureMode(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8891287)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    a3 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm1;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm1;
    v_stack_m40 = v_xmm0;
    v_stack_m30 = v_xmm1;
    result = VslpEnterIumSecureMode(2, 272, a3, v_stack_m88);
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = v_xmm1;
    *(unsigned __int64 *)(a1 + 64) = v_xmm0;
    *(unsigned __int64 *)(a1 + 80) = v_xmm1;
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 272, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslpKsrEnterIumSecureMode(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x87AB97)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    a3 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm1;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm1;
    v_stack_m40 = v_xmm0;
    v_stack_m30 = v_xmm1;
    result = VslpEnterIumSecureMode(2, 272, a3, v_stack_m88);
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(arg1 + 0x30) = v_xmm1;
    *(uint64_t *)(arg1 + 0x40) = v_xmm0;
    *(uint64_t *)(arg1 + 0x50) = v_xmm1;
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 272, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x30` | `128` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x50` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058FB90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058FB90[BB_0058FB90]
  bb_0058FC50[BB_0058FC50]
```
