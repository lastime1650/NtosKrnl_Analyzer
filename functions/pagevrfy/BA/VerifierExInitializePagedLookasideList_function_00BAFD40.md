# VerifierExInitializePagedLookasideList

- RVA: `0x00BAFD40`–`0x00BAFE00` (길이 `192` bytes)
- VA: `0x0000000140BAFD40`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071A74`
- 디코드: `42`개 명령, `192/192` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00BAFDA2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BAFD46` → RVA `0x00E681A0` (`.data`; read)
- `0x00BAFD50` → RVA `0x00FF4130` (`PAGEVRFD`; read)
- `0x00BAFD57` → RVA `0x00468040` (`ExInitializePagedLookasideListInternal`; read)
- `0x00BAFDB1` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x00BAFDC2` → RVA `0x00B82010` (`ExAllocatePoolWithTag`; read)
- `0x00BAFDCE` → RVA `0x00BA15B0` (`VerifierExAllocatePoolWithTag`; read)
- `0x00BAFDD7` → RVA `0x004987E0` (`ExAllocatePoolWithQuotaTag`; read)
- `0x00BAFDE3` → RVA `0x00BA1510` (`VerifierExAllocatePoolWithQuotaTag`; read)
- `0x00BAFDEE` → RVA `0x00BA1800` (`VerifierExFreePool`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BAFDA2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAFD40  40 53                           push rbx
00BAFD42  48 83 EC 50                     sub rsp, 0x50
00BAFD46  F6 05 53 84 2B 00 01            test byte ptr [rip + 0x2b8453], 1
00BAFD4D  48 8B D9                        mov rbx, rcx
00BAFD50  48 8B 05 D9 43 44 00            mov rax, qword ptr [rip + 0x4443d9]
00BAFD57  48 8D 0D E2 82 8B FF            lea rcx, [rip - 0x747d1e]
00BAFD5E  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00BAFD63  4C 8B DA                        mov r11, rdx
00BAFD66  8B 94 24 88 00 00 00            mov edx, dword ptr [rsp + 0x88]
00BAFD6D  41 BA 00 00 00 00               mov r10d, 0
00BAFD73  66 44 0F 44 94 24 90 00 00 00   cmove r10w, word ptr [rsp + 0x90]
00BAFD7D  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00BAFD85  C7 44 24 38 01 00 00 00         mov dword ptr [rsp + 0x38], 1
00BAFD8D  66 44 89 54 24 30               mov word ptr [rsp + 0x30], r10w
00BAFD93  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00BAFD97  49 8B D3                        mov rdx, r11
00BAFD9A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00BAFD9F  48 8B CB                        mov rcx, rbx
00BAFDA2  E8 29 AD B0 FF                  call 0x1406baad0
00BAFDA7  8B 05 F3 83 2B 00               mov eax, dword ptr [rip + 0x2b83f3]
00BAFDAD  A8 01                           test al, 1
00BAFDAF  74 48                           je 0x140bafdf9
00BAFDB1  48 8D 05 98 2A FD FF            lea rax, [rip - 0x2d568]
00BAFDB8  48 39 43 38                     cmp qword ptr [rbx + 0x38], rax
00BAFDBC  75 3B                           jne 0x140bafdf9
00BAFDBE  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00BAFDC2  48 8D 0D 47 22 FD FF            lea rcx, [rip - 0x2ddb9]
00BAFDC9  48 3B C1                        cmp rax, rcx
00BAFDCC  75 09                           jne 0x140bafdd7
00BAFDCE  48 8D 05 DB 17 FF FF            lea rax, [rip - 0xe825]
00BAFDD5  EB 13                           jmp 0x140bafdea
00BAFDD7  48 8D 0D 02 8A 8E FF            lea rcx, [rip - 0x7175fe]
00BAFDDE  48 3B C1                        cmp rax, rcx
00BAFDE1  75 16                           jne 0x140bafdf9
00BAFDE3  48 8D 05 26 17 FF FF            lea rax, [rip - 0xe8da]
00BAFDEA  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00BAFDEE  48 8D 05 0B 1A FF FF            lea rax, [rip - 0xe5f5]
00BAFDF5  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
00BAFDF9  48 83 C4 50                     add rsp, 0x50
00BAFDFD  5B                              pop rbx
00BAFDFE  C3                              ret
00BAFDFF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierExInitializePagedLookasideList(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned __int16 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int16 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (80);
    v_stack_m18 = v_rip - 7634206;
    v_r10 = 0;
    if (((*(unsigned __int8 *)(v_rip + 2851923)) & (1)) == 0) { v_r10 = a7; }
    v_stack_m20 = 1;
    v_stack_m28 = (unsigned __int16)(v_r10);
    v_stack_m30 = (unsigned int)((unsigned int)(a6));
    v_stack_m38 = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2851827)))) & (1)) == 0) goto loc_00BAFDF9;
    if ((*(unsigned __int64 *)(a1 + 56)) != (v_rip - 185704)) goto loc_00BAFDF9;
    if ((*(unsigned __int64 *)(a1 + 48)) != (v_rip - 187833)) goto loc_00BAFDD7;
    goto loc_00BAFDEA;
loc_00BAFDD7:
    if ((v_rip - 59429) != (v_rip - 7435774)) goto loc_00BAFDF9;
loc_00BAFDEA:
    *(unsigned __int64 *)(a1 + 48) = v_rip - 59610;
    *(unsigned __int64 *)(a1 + 56) = v_rip - 58869;
loc_00BAFDF9:
    v_rsp = (v_rsp) + (80);
    return v_rip - 58869;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierExInitializePagedLookasideList(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint16_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint16_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (80);
    v_stack_m18 = v_rip - 7634206;
    local_r10 = 0;
    if (((*(uint8_t *)(v_rip + 0x2B8453)) & (1)) == 0) { local_r10 = Arg7; }
    v_stack_m20 = 1;
    v_stack_m28 = (uint16_t)(local_r10);
    v_stack_m30 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m38 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2B83F3)))) & (1)) == 0) goto loc_00BAFDF9;
    if ((*(uint64_t *)(arg1 + 0x38)) != (v_rip - 185704)) goto loc_00BAFDF9;
    if ((*(uint64_t *)(arg1 + 0x30)) != (v_rip - 187833)) goto loc_00BAFDD7;
    goto loc_00BAFDEA;
loc_00BAFDD7:
    if ((v_rip - 59429) != (v_rip - 7435774)) goto loc_00BAFDF9;
loc_00BAFDEA:
    *(uint64_t *)(arg1 + 0x30) = v_rip - 59610;
    *(uint64_t *)(arg1 + 0x38) = v_rip - 58869;
loc_00BAFDF9:
    local_rsp = (local_rsp) + (80);
    return v_rip - 58869;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAFD40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAFD40[BB_00BAFD40]
  bb_00BAFDB1[BB_00BAFDB1]
  bb_00BAFDBE[BB_00BAFDBE]
  bb_00BAFDCE[BB_00BAFDCE]
  bb_00BAFDD7[BB_00BAFDD7]
  bb_00BAFDE3[BB_00BAFDE3]
  bb_00BAFDEA[BB_00BAFDEA]
  bb_00BAFDF9[BB_00BAFDF9]
  bb_00BAFDFF[BB_00BAFDFF]
  bb_00BAFD40 -->|branch| bb_00BAFDF9
  bb_00BAFD40 -->|fallthrough| bb_00BAFDB1
  bb_00BAFDB1 -->|branch| bb_00BAFDF9
  bb_00BAFDB1 -->|fallthrough| bb_00BAFDBE
  bb_00BAFDBE -->|branch| bb_00BAFDD7
  bb_00BAFDBE -->|fallthrough| bb_00BAFDCE
  bb_00BAFDCE -->|branch| bb_00BAFDEA
  bb_00BAFDD7 -->|branch| bb_00BAFDF9
  bb_00BAFDD7 -->|fallthrough| bb_00BAFDE3
  bb_00BAFDE3 -->|flow| bb_00BAFDEA
  bb_00BAFDEA -->|flow| bb_00BAFDF9
```
