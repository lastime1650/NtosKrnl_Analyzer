# EtwTraceJobSendNotification

- RVA: `0x0091713C`–`0x009171CC` (길이 `144` bytes)
- VA: `0x000000014091713C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A998`
- 디코드: `31`개 명령, `144/144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009171AD` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x009171BA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PspSendReliableJobNotification](PspSendReliableJobNotification_function_009171D4.md) at `0x0091724A`

### Static image references
- `0x00917140` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009171AD` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (`PAGE` → `.text`)
  - `0x009171BA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0091713C  48 83 EC 68                     sub rsp, 0x68
00917140  48 8B 05 F9 35 4F 00            mov rax, qword ptr [rip + 0x4f35f9]
00917147  48 33 C4                        xor rax, rsp
0091714A  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0091714F  45 33 C0                        xor r8d, r8d
00917152  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
00917157  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0091715C  48 85 C9                        test rcx, rcx
0091715F  74 64                           je 0x1409171c5
00917161  0F 10 81 C0 05 00 00            movups xmm0, xmmword ptr [rcx + 0x5c0]
00917168  8B 81 BC 05 00 00               mov eax, dword ptr [rcx + 0x5bc]
0091716E  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00917172  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
00917178  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0091717C  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00917181  BA 01 00 00 00                  mov edx, 1
00917186  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0091718B  41 B9 2A 07 00 00               mov r9d, 0x72a
00917191  48 C7 44 24 50 18 00 00 00      mov qword ptr [rsp + 0x50], 0x18
0091719A  41 B8 00 00 08 00               mov r8d, 0x80000
009171A0  C7 44 24 20 04 19 60 00         mov dword ptr [rsp + 0x20], 0x601904
009171A8  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
009171AD  E8 9E E1 91 FF                  call 0x140235350
009171B2  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009171B7  48 33 CC                        xor rcx, rsp
009171BA  E8 81 54 D9 FF                  call 0x1406ac640
009171BF  48 83 C4 68                     add rsp, 0x68
009171C3  C3                              ret
009171C4  CC                              int3
009171C5  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
009171CA  EB AC                           jmp 0x140917178
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceJobSendNotification(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m48;
    unsigned int v_stack_p40;

    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 5191161)) ^ (v_rsp);
    v_stack_m10 = result;
    a3 = 0;
    v_stack_m38 = 0;
    v_stack_m30 = 0;
    if (a1 == 0) goto loc_009171C5;
    v_stack_m28 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1468)));
    v_stack_m38 = v_xmm0;
loc_00917178:
    v_stack_m24 = a2;
    v_stack_m20 = v_stack_m38;
    v_stack_m18 = 24;
    v_stack_m48 = 0x601904ULL;
    result = EtwTraceKernelEvent(v_stack_m20, 1, (unsigned int)(0x80000ULL), (unsigned int)(0x72AULL));
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0x80000ULL), (unsigned int)(0x72AULL));
    v_rsp = (v_rsp) + (104);
    return result;
loc_009171C5:
    v_stack_p40 = (unsigned int)((unsigned int)(0x80000ULL));
    goto loc_00917178;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceJobSendNotification(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m48;
    uint32_t v_stack_p40;

    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x4F35F9)) ^ (local_rsp);
    v_stack_m10 = result;
    Arg3 = 0;
    v_stack_m38 = 0;
    v_stack_m30 = 0;
    if (Arg1 == 0) goto loc_009171C5;
    v_stack_m28 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x5BC)));
    v_stack_m38 = v_xmm0;
loc_00917178:
    v_stack_m24 = Arg2;
    v_stack_m20 = v_stack_m38;
    v_stack_m18 = 24;
    v_stack_m48 = 0x601904ULL;
    result = EtwTraceKernelEvent(v_stack_m20, 1, (uint32_t)(0x80000ULL), (uint32_t)(0x72AULL));
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0x80000ULL), (uint32_t)(0x72AULL));
    local_rsp = (local_rsp) + (104);
    return result;
loc_009171C5:
    v_stack_p40 = (uint32_t)((uint32_t)(0x80000ULL));
    goto loc_00917178;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091713C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0091713C[BB_0091713C]
  bb_00917161[BB_00917161]
  bb_00917178[BB_00917178]
  bb_009171C4[BB_009171C4]
  bb_009171C5[BB_009171C5]
  bb_0091713C -->|branch| bb_009171C5
  bb_0091713C -->|fallthrough| bb_00917161
  bb_00917161 -->|flow| bb_00917178
  bb_009171C4 -->|flow| bb_009171C5
  bb_009171C5 -->|branch| bb_00917178
```
