# PnpOpenCCSPnpRegKey

- RVA: `0x00C33658`–`0x00C336DC` (길이 `132` bytes)
- VA: `0x0000000140C33658`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F554`
- 디코드: `34`개 명령, `132/132` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00C33681` → [_PnpCtxGetCachedContextBaseKey](../../page/8E/_PnpCtxGetCachedContextBaseKey_function_008EFB2C.md) (function, `0x008EFB2C`)
- `0x00C336C0` → [IopCreateRegistryKeyEx](../../page/A8/IopCreateRegistryKeyEx_function_00A89038.md) (function, `0x00A89038`)

### Direct callers
- [PnpInitializePnpWatchdogs](PnpInitializePnpWatchdogs_function_00C3357C.md) at `0x00C3358B`

### Static image references
- `0x00C33670` → RVA `0x00E66398` (`.data`; read)
- `0x00C33692` → RVA `0x00C79EA0` (` ?? ::PBOPGDP::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C33681` → [_PnpCtxGetCachedContextBaseKey](../../page/8E/_PnpCtxGetCachedContextBaseKey_function_008EFB2C.md) (`INIT` → `PAGE`)
  - `0x00C336C0` → [IopCreateRegistryKeyEx](../../page/A8/IopCreateRegistryKeyEx_function_00A89038.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C33658  48 8B C4                        mov rax, rsp
00C3365B  53                              push rbx
00C3365C  48 83 EC 40                     sub rsp, 0x40
00C33660  83 60 EC 00                     and dword ptr [rax - 0x14], 0
00C33664  4C 8D 40 18                     lea r8, [rax + 0x18]
00C33668  48 83 60 18 00                  and qword ptr [rax + 0x18], 0
00C3366D  48 8B D9                        mov rbx, rcx
00C33670  48 8B 0D 21 2D 23 00            mov rcx, qword ptr [rip + 0x232d21]
00C33677  BA 04 00 00 00                  mov edx, 4
00C3367C  48 83 60 20 00                  and qword ptr [rax + 0x20], 0
00C33681  E8 A6 C4 CB FF                  call 0x1408efb2c
00C33686  8B D0                           mov edx, eax
00C33688  85 C0                           test eax, eax
00C3368A  78 47                           js 0x140c336d3
00C3368C  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00C33692  48 8D 05 07 68 04 00            lea rax, [rip + 0x46807]
00C33699  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00C3369E  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00C336A3  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00C336A8  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00C336AD  41 B9 01 00 00 00               mov r9d, 1
00C336B3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00C336B8  C7 44 24 30 16 00 18 00         mov dword ptr [rsp + 0x30], 0x180016
00C336C0  E8 73 59 E5 FF                  call 0x140a89038
00C336C5  8B D0                           mov edx, eax
00C336C7  85 C0                           test eax, eax
00C336C9  78 08                           js 0x140c336d3
00C336CB  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00C336D0  48 89 03                        mov qword ptr [rbx], rax
00C336D3  8B C2                           mov eax, edx
00C336D5  48 83 C4 40                     add rsp, 0x40
00C336D9  5B                              pop rbx
00C336DA  C3                              ret
00C336DB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpOpenCCSPnpRegKey(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (64);
    result = _PnpCtxGetCachedContextBaseKey(*(unsigned __int64 *)(v_rip + 2305313), 4, v_rsp + 24, a4);
    if (sign_flag) goto loc_00C336D3;
    v_stack_m10 = v_rip + 288775;
    v_stack_m18 = 0x180016ULL;
    result = IopCreateRegistryKeyEx(v_stack_p20, v_stack_p18, v_stack_m18, 1);
    if (!(sign_flag)) {
        result = v_stack_p20;
        *(unsigned __int64 *)(a1) = result;
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t PnpOpenCCSPnpRegKey(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (64);
    result = _PnpCtxGetCachedContextBaseKey(*(uint64_t *)(v_rip + 0x232D21), 4, local_rsp + 24, a4);
    if (sign_flag) goto loc_00C336D3;
    v_stack_m10 = v_rip + 288775;
    v_stack_m18 = 0x180016ULL;
    result = IopCreateRegistryKeyEx(v_stack_p20, v_stack_p18, v_stack_m18, 1);
    if (!(sign_flag)) {
        result = v_stack_p20;
        *(uint64_t *)(arg1) = result;
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C33658&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C33658[BB_00C33658]
  bb_00C3368C[BB_00C3368C]
  bb_00C336CB[BB_00C336CB]
  bb_00C336D3[BB_00C336D3]
  bb_00C336DB[BB_00C336DB]
  bb_00C33658 -->|branch| bb_00C336D3
  bb_00C33658 -->|fallthrough| bb_00C3368C
  bb_00C3368C -->|branch| bb_00C336D3
  bb_00C3368C -->|fallthrough| bb_00C336CB
  bb_00C336CB -->|flow| bb_00C336D3
```
