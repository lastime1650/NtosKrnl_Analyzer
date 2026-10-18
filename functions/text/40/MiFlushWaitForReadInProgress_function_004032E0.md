# MiFlushWaitForReadInProgress

- RVA: `0x004032E0`–`0x00403384` (길이 `164` bytes)
- VA: `0x00000001404032E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A704`
- 디코드: `42`개 명령, `164/164` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00403313` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0040333A` → [MiInitializePageFaultPacket](../22/MiInitializePageFaultPacket_function_00228EB0.md) (function, `0x00228EB0`)
- `0x00403346` → [MiObtainProtoReference](../31/MiObtainProtoReference_function_00318178.md) (function, `0x00318178`)
- `0x00403363` → [MiWaitForCollidedFaultComplete](../36/MiWaitForCollidedFaultComplete_function_00369EDC.md) (function, `0x00369EDC`)
- `0x00403373` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiFlushSection](MiFlushSection_function_004036B0.md) at `0x00404368`

### Static image references
- `0x004032EB` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004032E0  40 53                           push rbx
004032E2  56                              push rsi
004032E3  57                              push rdi
004032E4  48 81 EC F0 00 00 00            sub rsp, 0xf0
004032EB  48 8B 05 4E 74 A0 00            mov rax, qword ptr [rip + 0xa0744e]
004032F2  48 33 C4                        xor rax, rsp
004032F5  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
004032FD  41 8A F0                        mov sil, r8b
00403300  48 8B FA                        mov rdi, rdx
00403303  48 8B D9                        mov rbx, rcx
00403306  33 D2                           xor edx, edx
00403308  41 B8 98 00 00 00               mov r8d, 0x98
0040330E  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00403313  E8 28 39 2C 00                  call 0x1406c6c40
00403318  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0040331D  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00403325  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0040332A  45 33 C9                        xor r9d, r9d
0040332D  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00403333  45 33 C0                        xor r8d, r8d
00403336  33 D2                           xor edx, edx
00403338  33 C9                           xor ecx, ecx
0040333A  E8 71 5B E2 FF                  call 0x140228eb0
0040333F  41 8D 51 01                     lea edx, [r9 + 1]
00403343  48 8B CF                        mov rcx, rdi
00403346  E8 2D 4E F1 FF                  call 0x140318178
0040334B  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00403350  44 8A CE                        mov r9b, sil
00403353  4C 8B C7                        mov r8, rdi
00403356  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0040335B  48 8B D3                        mov rdx, rbx
0040335E  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00403363  E8 74 6B F6 FF                  call 0x140369edc
00403368  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00403370  48 33 CC                        xor rcx, rsp
00403373  E8 C8 92 2A 00                  call 0x1406ac640
00403378  48 81 C4 F0 00 00 00            add rsp, 0xf0
0040337F  5F                              pop rdi
00403380  5E                              pop rsi
00403381  5B                              pop rbx
00403382  C3                              ret
00403383  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFlushWaitForReadInProgress(__int64 a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;

    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 10515534)) ^ (v_rsp);
    v_stack_m28 = result;
    a2 = 0;
    result = memset(v_stack_mC8, a2, 152, a4);
    v_stack_mD8 = 1;
    v_stack_mE0 = v_stack_mC8;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = MiInitializePageFaultPacket(a1, a2, a3, a4);
    result = MiObtainProtoReference(0, a4 + 1, a3, a4);
    v_stack_mE8 = v_stack_mD8;
    result = MiWaitForCollidedFaultComplete(v_stack_mC8, 0, 0, 0);
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, 0, 0, 0);
    v_rsp = (v_rsp) + (240);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiFlushWaitForReadInProgress(int64_t Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;

    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0xA0744E)) ^ (local_rsp);
    v_stack_m28 = result;
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 152, Arg4);
    v_stack_mD8 = 1;
    v_stack_mE0 = v_stack_mC8;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = MiInitializePageFaultPacket(Arg1, Arg2, Arg3, Arg4);
    result = MiObtainProtoReference(0, Arg4 + 1, Arg3, Arg4);
    v_stack_mE8 = v_stack_mD8;
    result = MiWaitForCollidedFaultComplete(v_stack_mC8, 0, 0, 0);
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 0, 0, 0);
    local_rsp = (local_rsp) + (240);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004032E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004032E0[BB_004032E0]
  bb_00403383[BB_00403383]
```
