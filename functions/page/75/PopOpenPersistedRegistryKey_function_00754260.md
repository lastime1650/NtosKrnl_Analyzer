# PopOpenPersistedRegistryKey

- RVA: `0x00754260`–`0x0075436D` (길이 `269` bytes)
- VA: `0x0000000140754260`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CBD68`
- 디코드: `60`개 명령, `269/269` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007542D3` → [RtlGetPersistedStateLocation](../8C/RtlGetPersistedStateLocation_function_008C8DE0.md) (function, `0x008C8DE0`)
- `0x007542E7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00754337` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00754356` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopLidReliabilityInit](../../text/5D/PopLidReliabilityInit_function_005D5308.md) at `0x005D5346`
- [PopSaveLidReliabilityState](PopSaveLidReliabilityState_function_0075F1E8.md) at `0x0075F1FF`

### Static image references
- `0x00754275` → RVA `0x00E0A740` (`.data`; read)
- `0x0075428C` → RVA `0x00029610` (`.rdata`; read)
- `0x00754295` → RVA `0x00029350` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007542E7` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00754337` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x00754356` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00754260  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00754265  55                              push rbp
00754266  48 8D AC 24 50 FE FF FF         lea rbp, [rsp - 0x1b0]
0075426E  48 81 EC B0 02 00 00            sub rsp, 0x2b0
00754275  48 8B 05 C4 64 6B 00            mov rax, qword ptr [rip + 0x6b64c4]
0075427C  48 33 C4                        xor rax, rsp
0075427F  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
00754286  48 83 64 24 40 00               and qword ptr [rsp + 0x40], 0
0075428C  4C 8D 05 7D 53 8D FF            lea r8, [rip - 0x72ac83]
00754293  33 C0                           xor eax, eax
00754295  48 8D 0D B4 50 8D FF            lea rcx, [rip - 0x72af4c]
0075429C  21 44 24 7C                     and dword ptr [rsp + 0x7c], eax
007542A0  48 8B DA                        mov rbx, rdx
007542A3  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
007542A7  0F 57 C0                        xorps xmm0, xmm0
007542AA  21 44 24 64                     and dword ptr [rsp + 0x64], eax
007542AE  45 33 C9                        xor r9d, r9d
007542B1  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007542B6  33 D2                           xor edx, edx
007542B8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007542BD  48 8D 45 90                     lea rax, [rbp - 0x70]
007542C1  C7 44 24 28 08 02 00 00         mov dword ptr [rsp + 0x28], 0x208
007542C9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007542CE  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
007542D3  E8 08 4B 17 00                  call 0x1408c8de0
007542D8  8B C8                           mov ecx, eax
007542DA  85 C0                           test eax, eax
007542DC  78 6C                           js 0x14075434a
007542DE  48 8D 55 90                     lea rdx, [rbp - 0x70]
007542E2  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007542E7  E8 94 64 CD FF                  call 0x14042a780
007542EC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
007542F2  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007542F7  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
007542FC  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00754301  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
00754307  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0075430C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00754312  0F 57 C0                        xorps xmm0, xmm0
00754315  45 33 C9                        xor r9d, r9d
00754318  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0075431D  BA 1F 00 02 00                  mov edx, 0x2001f
00754322  C7 44 24 60 30 00 00 00         mov dword ptr [rsp + 0x60], 0x30
0075432A  F3 0F 7F 45 80                  movdqu xmmword ptr [rbp - 0x80], xmm0
0075432F  C7 44 24 78 40 02 00 00         mov dword ptr [rsp + 0x78], 0x240
00754337  E8 34 91 F5 FF                  call 0x1406ad470
0075433C  8B C8                           mov ecx, eax
0075433E  85 C0                           test eax, eax
00754340  78 08                           js 0x14075434a
00754342  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00754347  48 89 03                        mov qword ptr [rbx], rax
0075434A  8B C1                           mov eax, ecx
0075434C  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
00754353  48 33 CC                        xor rcx, rsp
00754356  E8 E5 82 F5 FF                  call 0x1406ac640
0075435B  48 8B 9C 24 C0 02 00 00         mov rbx, qword ptr [rsp + 0x2c0]
00754363  48 81 C4 B0 02 00 00            add rsp, 0x2b0
0075436A  5D                              pop rbp
0075436B  C3                              ret
0075436C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopOpenPersistedRegistryKey(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m23C;
    unsigned int v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m254;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m288;
    unsigned int v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (688);
    result = (*(unsigned __int64 *)(v_rip + 7038148)) ^ (v_rsp);
    v_stack_m18 = result;
    result = 0;
    v_stack_m254 = 0;
    a4 = 0;
    a2 = 0;
    v_stack_m288 = v_stack_m270;
    v_stack_m290 = 520;
    v_stack_m298 = v_stack_m228;
    v_stack_m268 = v_xmm0;
    result = RtlGetPersistedStateLocation(v_rip - 7515980, a2, v_rip - 7515267, a4);
    if (sign_flag) goto loc_0075434A;
    result = RtlInitUnicodeString(v_stack_m268, v_stack_m228, v_rip - 7515267, a4);
    a4 = 0;
    v_stack_m248 = v_stack_m268;
    v_stack_m258 = 48;
    v_stack_m238 = v_xmm0;
    v_stack_m240 = 576;
    result = ZwCreateKey(v_stack_m278, (unsigned int)(0x2001FULL), v_stack_m258, a4);
    if (!(sign_flag)) {
        result = v_stack_m278;
        *(unsigned __int64 *)(a2) = result;
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x2001FULL), v_stack_m258, a4);
    v_rsp = (v_rsp) + (688);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopOpenPersistedRegistryKey(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m228;
    uint64_t v_stack_m238;
    uint32_t v_stack_m23C;
    uint32_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint32_t v_stack_m254;
    uint64_t v_stack_m258;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m288;
    uint32_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (688);
    result = (*(uint64_t *)(v_rip + 0x6B64C4)) ^ (local_rsp);
    v_stack_m18 = result;
    result = 0;
    v_stack_m254 = 0;
    Arg4 = 0;
    Arg2 = 0;
    v_stack_m288 = v_stack_m270;
    v_stack_m290 = 520;
    v_stack_m298 = v_stack_m228;
    v_stack_m268 = v_xmm0;
    result = RtlGetPersistedStateLocation(v_rip - 7515980, Arg2, v_rip - 7515267, Arg4);
    if (sign_flag) goto loc_0075434A;
    result = RtlInitUnicodeString(v_stack_m268, v_stack_m228, v_rip - 7515267, Arg4);
    Arg4 = 0;
    v_stack_m248 = v_stack_m268;
    v_stack_m258 = 48;
    v_stack_m238 = v_xmm0;
    v_stack_m240 = 576;
    result = ZwCreateKey(v_stack_m278, (uint32_t)(0x2001FULL), v_stack_m258, Arg4);
    if (!(sign_flag)) {
        result = v_stack_m278;
        *(uint64_t *)(arg2) = result;
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x2001FULL), v_stack_m258, Arg4);
    local_rsp = (local_rsp) + (688);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00754260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00754260[BB_00754260]
  bb_007542DE[BB_007542DE]
  bb_00754342[BB_00754342]
  bb_0075434A[BB_0075434A]
  bb_0075436C[BB_0075436C]
  bb_00754260 -->|branch| bb_0075434A
  bb_00754260 -->|fallthrough| bb_007542DE
  bb_007542DE -->|branch| bb_0075434A
  bb_007542DE -->|fallthrough| bb_00754342
  bb_00754342 -->|flow| bb_0075434A
```
