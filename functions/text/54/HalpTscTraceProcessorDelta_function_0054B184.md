# HalpTscTraceProcessorDelta

- RVA: `0x0054B184`–`0x0054B260` (길이 `220` bytes)
- VA: `0x000000014054B184`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A288`
- 디코드: `52`개 명령, `220/220` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0054B1CA` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0054B245` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x0054B251` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HalpTscAdvSynchCalculateRemoteDeltas](HalpTscAdvSynchCalculateRemoteDeltas_function_0054A5B0.md) at `0x0054A654`

### Static image references
- `0x0054B1A1` → RVA `0x00E0A740` (`.data`; read)
- `0x0054B1AF` → RVA `0x00FC22C0` (`.data`; read)
- `0x0054B1BC` → RVA `0x00FC22B8` (`.data`; read)
- `0x0054B1C3` → RVA `0x00022C20` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054B184  48 8B C4                        mov rax, rsp
0054B187  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
0054B18B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0054B18F  89 50 10                        mov dword ptr [rax + 0x10], edx
0054B192  89 48 08                        mov dword ptr [rax + 8], ecx
0054B195  55                              push rbp
0054B196  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0054B19A  48 81 EC 90 00 00 00            sub rsp, 0x90
0054B1A1  48 8B 05 98 F5 8B 00            mov rax, qword ptr [rip + 0x8bf598]
0054B1A8  48 33 C4                        xor rax, rsp
0054B1AB  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0054B1AF  80 3D 0A 71 A7 00 00            cmp byte ptr [rip + 0xa7710a], 0
0054B1B6  0F 84 8E 00 00 00               je 0x14054b24a
0054B1BC  48 8B 0D F5 70 A7 00            mov rcx, qword ptr [rip + 0xa770f5]
0054B1C3  48 8D 15 56 7A AD FF            lea rdx, [rip - 0x5285aa]
0054B1CA  E8 81 72 E4 FF                  call 0x140392450
0054B1CF  84 C0                           test al, al
0054B1D1  74 77                           je 0x14054b24a
0054B1D3  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0054B1D7  48 8D 45 67                     lea rax, [rbp + 0x67]
0054B1DB  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0054B1DF  48 8D 15 3A 7A AD FF            lea rdx, [rip - 0x5285c6]
0054B1E6  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0054B1EA  B9 04 00 00 00                  mov ecx, 4
0054B1EF  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0054B1F3  45 33 C9                        xor r9d, r9d
0054B1F6  48 89 45 07                     mov qword ptr [rbp + 7], rax
0054B1FA  45 33 C0                        xor r8d, r8d
0054B1FD  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0054B201  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
0054B204  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0054B208  48 8D 45 77                     lea rax, [rbp + 0x77]
0054B20C  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0054B210  48 8D 45 7F                     lea rax, [rbp + 0x7f]
0054B214  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0054B218  48 8D 45 07                     lea rax, [rbp + 7]
0054B21C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0054B221  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0054B225  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0054B22B  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0054B231  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
0054B234  89 4D 3F                        mov dword ptr [rbp + 0x3f], ecx
0054B237  48 8B 0D 7A 70 A7 00            mov rcx, qword ptr [rip + 0xa7707a]
0054B23E  C7 45 2F 08 00 00 00            mov dword ptr [rbp + 0x2f], 8
0054B245  E8 86 3E D1 FF                  call 0x14025f0d0
0054B24A  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0054B24E  48 33 CC                        xor rcx, rsp
0054B251  E8 EA 13 16 00                  call 0x1406ac640
0054B256  48 81 C4 90 00 00 00            add rsp, 0x90
0054B25D  5D                              pop rbp
0054B25E  C3                              ret
0054B25F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTscTraceProcessorDelta(int a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 9172376)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned __int8 *)(v_rip + 10973450)) == 0) goto loc_0054B24A;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10973429), v_rip - 5408170, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 95 + 103;
        a2 = v_rip - 5408198;
        a1 = 4;
        a4 = 0;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        a3 = 0;
        result = v_rsp - 95 + 111;
        *(unsigned int *)(v_rsp - 95 + 15) = a1;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 + 119;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 + 127;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 + 7;
        v_stack_m60 = result;
        v_stack_m68 = a1;
        *(unsigned int *)(v_rsp - 95 + 31) = a1;
        *(unsigned int *)(v_rsp - 95 + 63) = a1;
        a1 = *(unsigned __int64 *)(v_rip + 10973306);
        *(unsigned int *)(v_rsp - 95 + 47) = 8;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpTscTraceProcessorDelta(int32_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x8BF598)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint8_t *)(v_rip + 0xA7710A)) == 0) goto loc_0054B24A;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA770F5), v_rip - 5408170, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 95 + 103;
        Arg2 = v_rip - 5408198;
        Arg1 = 4;
        Arg4 = 0;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        Arg3 = 0;
        result = local_rsp - 95 + 111;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = Arg1;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 + 119;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 + 127;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 + 7;
        v_stack_m60 = result;
        v_stack_m68 = Arg1;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg1;
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0xA7707A);
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = 8;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054B184&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054B184[BB_0054B184]
  bb_0054B1BC[BB_0054B1BC]
  bb_0054B1D3[BB_0054B1D3]
  bb_0054B24A[BB_0054B24A]
  bb_0054B25F[BB_0054B25F]
  bb_0054B184 -->|branch| bb_0054B24A
  bb_0054B184 -->|fallthrough| bb_0054B1BC
  bb_0054B1BC -->|branch| bb_0054B24A
  bb_0054B1BC -->|fallthrough| bb_0054B1D3
  bb_0054B1D3 -->|flow| bb_0054B24A
```
