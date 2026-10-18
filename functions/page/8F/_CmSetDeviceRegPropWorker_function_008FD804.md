# _CmSetDeviceRegPropWorker

- RVA: `0x008FD804`–`0x008FDB0A` (길이 `774` bytes)
- VA: `0x00000001408FD804`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00088144`
- 디코드: `195`개 명령, `774/774` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008FD8A3` → [_CmDevicePropertyWrite](../../text/49/_CmDevicePropertyWrite_function_004941AC.md) (function, `0x004941AC`)
- `0x008FD8B2` → [MapCmDevicePropertyToRegType](../../text/47/MapCmDevicePropertyToRegType_function_0047AE40.md) (function, `0x0047AE40`)
- `0x008FD8FB` → [MapCmDevicePropertyToRegValue](../../text/44/MapCmDevicePropertyToRegValue_function_004466E0.md) (function, `0x004466E0`)
- `0x008FD91C` → [PnpCtxRegDeleteValue](PnpCtxRegDeleteValue_function_008FE5E0.md) (function, `0x008FE5E0`)
- `0x008FD997` → [PnpCtxRegSetValue](../99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x008FD9C7` → [CmRaisePropertyChangeEvent](CmRaisePropertyChangeEvent_function_008FE93C.md) (function, `0x008FE93C`)
- `0x008FDA33` → [RtlValidRelativeSecurityDescriptor](../8B/RtlValidRelativeSecurityDescriptor_function_008BDC70.md) (function, `0x008BDC70`)
- `0x008FDA43` → [RtlLengthSecurityDescriptor](../8B/RtlLengthSecurityDescriptor_function_008BC870.md) (function, `0x008BC870`)
- `0x008FDA8F` → [CmIsRootDevice](../93/CmIsRootDevice_function_009325E4.md) (function, `0x009325E4`)
- `0x008FDADC` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x008FDB00` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [CmSetDeviceRegProp](CmSetDeviceRegProp_function_008FD68C.md) at `0x008FD78C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x008FD8A3` → [_CmDevicePropertyWrite](../../text/49/_CmDevicePropertyWrite_function_004941AC.md) (`PAGE` → `.text`)
  - `0x008FD8B2` → [MapCmDevicePropertyToRegType](../../text/47/MapCmDevicePropertyToRegType_function_0047AE40.md) (`PAGE` → `.text`)
  - `0x008FD8FB` → [MapCmDevicePropertyToRegValue](../../text/44/MapCmDevicePropertyToRegValue_function_004466E0.md) (`PAGE` → `.text`)
  - `0x008FDB00` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x008FD864` → [sub_00B1FD16](../B1/Unknown_function_00B1FD16.md) (`tail-transfer`)
  - `0x008FDA3A` → [sub_00B1FD16 + 0x72](../B1/Unknown_function_00B1FD16.md) (`tail-transfer`)
  - `0x008FDA50` → [sub_00B1FD16 + 0x72](../B1/Unknown_function_00B1FD16.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008FD804  48 8B C4                        mov rax, rsp
008FD807  48 89 58 08                     mov qword ptr [rax + 8], rbx
008FD80B  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
008FD80F  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
008FD813  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
008FD817  41 54                           push r12
008FD819  41 56                           push r14
008FD81B  41 57                           push r15
008FD81D  48 83 EC 50                     sub rsp, 0x50
008FD821  33 DB                           xor ebx, ebx
008FD823  41 8B F9                        mov edi, r9d
008FD826  48 21 58 D8                     and qword ptr [rax - 0x28], rbx
008FD82A  4D 8B F0                        mov r14, r8
008FD82D  0F B7 84 24 A8 00 00 00         movzx eax, word ptr [rsp + 0xa8]
008FD835  4C 8B FA                        mov r15, rdx
008FD838  4C 8B E1                        mov r12, rcx
008FD83B  85 C0                           test eax, eax
008FD83D  0F 85 35 01 00 00               jne 0x1408fd978
008FD843  8B B4 24 A0 00 00 00            mov esi, dword ptr [rsp + 0xa0]
008FD84A  85 F6                           test esi, esi
008FD84C  0F 85 15 01 00 00               jne 0x1408fd967
008FD852  33 ED                           xor ebp, ebp
008FD854  41 8D 41 FF                     lea eax, [r9 - 1]
008FD858  83 F8 24                        cmp eax, 0x24
008FD85B  0F 87 B8 01 00 00               ja 0x1408fda19
008FD861  83 FF 13                        cmp edi, 0x13
008FD864  0F 8E AC 24 22 00               jle 0x140b1fd16
008FD86A  83 FF 1D                        cmp edi, 0x1d
008FD86D  0F 8E 68 01 00 00               jle 0x1408fd9db
008FD873  8B CF                           mov ecx, edi
008FD875  83 E9 1E                        sub ecx, 0x1e
008FD878  74 27                           je 0x1408fd8a1
008FD87A  83 E9 01                        sub ecx, 1
008FD87D  74 22                           je 0x1408fd8a1
008FD87F  83 E9 01                        sub ecx, 1
008FD882  74 1D                           je 0x1408fd8a1
008FD884  83 E9 01                        sub ecx, 1
008FD887  74 18                           je 0x1408fd8a1
008FD889  83 E9 01                        sub ecx, 1
008FD88C  74 13                           je 0x1408fd8a1
008FD88E  83 E9 01                        sub ecx, 1
008FD891  74 0E                           je 0x1408fd8a1
008FD893  83 E9 01                        sub ecx, 1
008FD896  74 09                           je 0x1408fd8a1
008FD898  83 F9 01                        cmp ecx, 1
008FD89B  0F 85 78 01 00 00               jne 0x1408fda19
008FD8A1  8B D7                           mov edx, edi
008FD8A3  E8 04 69 B9 FF                  call 0x1404941ac
008FD8A8  84 C0                           test al, al
008FD8AA  0F 84 A5 01 00 00               je 0x1408fda55
008FD8B0  8B CF                           mov ecx, edi
008FD8B2  E8 89 D5 B7 FF                  call 0x14047ae40
008FD8B7  85 C0                           test eax, eax
008FD8B9  0F 84 A0 01 00 00               je 0x1408fda5f
008FD8BF  39 84 24 90 00 00 00            cmp dword ptr [rsp + 0x90], eax
008FD8C6  0F 85 AC 00 00 00               jne 0x1408fd978
008FD8CC  83 FF 08                        cmp edi, 8
008FD8CF  0F 84 D1 01 00 00               je 0x1408fdaa6
008FD8D5  83 FF 0B                        cmp edi, 0xb
008FD8D8  0F 84 8B 01 00 00               je 0x1408fda69
008FD8DE  83 FF 18                        cmp edi, 0x18
008FD8E1  0F 84 3C 01 00 00               je 0x1408fda23
008FD8E7  4D 85 F6                        test r14, r14
008FD8EA  0F 84 C4 01 00 00               je 0x1408fdab4
008FD8F0  83 FF 08                        cmp edi, 8
008FD8F3  0F 84 B2 00 00 00               je 0x1408fd9ab
008FD8F9  8B D7                           mov edx, edi
008FD8FB  E8 E0 8D B4 FF                  call 0x1404466e0
008FD900  48 85 C0                        test rax, rax
008FD903  0F 84 10 01 00 00               je 0x1408fda19
008FD909  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
008FD90E  4C 8B C0                        mov r8, rax
008FD911  85 F6                           test esi, esi
008FD913  75 6A                           jne 0x1408fd97f
008FD915  4D 85 F6                        test r14, r14
008FD918  49 0F 45 D6                     cmovne rdx, r14
008FD91C  E8 BF 0C 00 00                  call 0x1408fe5e0
008FD921  8B D8                           mov ebx, eax
008FD923  3D 34 00 00 C0                  cmp eax, 0xc0000034
008FD928  0F 85 C2 01 00 00               jne 0x1408fdaf0
008FD92E  BB 25 02 00 C0                  mov ebx, 0xc0000225
008FD933  85 DB                           test ebx, ebx
008FD935  79 74                           jns 0x1408fd9ab
008FD937  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
008FD93C  48 85 C9                        test rcx, rcx
008FD93F  0F 85 BB 01 00 00               jne 0x1408fdb00
008FD945  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
008FD94A  8B C3                           mov eax, ebx
008FD94C  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
008FD950  49 8B 6B 28                     mov rbp, qword ptr [r11 + 0x28]
008FD954  49 8B 73 30                     mov rsi, qword ptr [r11 + 0x30]
008FD958  49 8B 7B 38                     mov rdi, qword ptr [r11 + 0x38]
008FD95C  49 8B E3                        mov rsp, r11
008FD95F  41 5F                           pop r15
008FD961  41 5E                           pop r14
008FD963  41 5C                           pop r12
008FD965  C3                              ret
008FD966  CC                              int3
008FD967  48 8B AC 24 98 00 00 00         mov rbp, qword ptr [rsp + 0x98]
008FD96F  48 85 ED                        test rbp, rbp
008FD972  0F 85 DC FE FF FF               jne 0x1408fd854
008FD978  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008FD97D  EB C6                           jmp 0x1408fd945
008FD97F  44 8B 8C 24 90 00 00 00         mov r9d, dword ptr [rsp + 0x90]
008FD987  4D 85 F6                        test r14, r14
008FD98A  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
008FD98E  49 0F 45 D6                     cmovne rdx, r14
008FD992  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
008FD997  E8 F0 41 09 00                  call 0x140991b8c
008FD99C  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008FD9A1  74 2E                           je 0x1408fd9d1
008FD9A3  85 C0                           test eax, eax
008FD9A5  79 8C                           jns 0x1408fd933
008FD9A7  8B D8                           mov ebx, eax
008FD9A9  EB 8C                           jmp 0x1408fd937
008FD9AB  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
008FD9B0  4D 85 F6                        test r14, r14
008FD9B3  41 B8 01 00 00 00               mov r8d, 1
008FD9B9  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
008FD9BD  4D 0F 45 CE                     cmovne r9, r14
008FD9C1  49 8B D7                        mov rdx, r15
008FD9C4  49 8B CC                        mov rcx, r12
008FD9C7  E8 70 0F 00 00                  call 0x1408fe93c
008FD9CC  E9 66 FF FF FF                  jmp 0x1408fd937
008FD9D1  BB 0E 00 00 C0                  mov ebx, 0xc000000e
008FD9D6  E9 5C FF FF FF                  jmp 0x1408fd937
008FD9DB  0F 84 C0 FE FF FF               je 0x1408fd8a1
008FD9E1  8B CF                           mov ecx, edi
008FD9E3  83 E9 14                        sub ecx, 0x14
008FD9E6  0F 84 B5 FE FF FF               je 0x1408fd8a1
008FD9EC  83 E9 01                        sub ecx, 1
008FD9EF  0F 84 AC FE FF FF               je 0x1408fd8a1
008FD9F5  83 E9 01                        sub ecx, 1
008FD9F8  0F 84 A3 FE FF FF               je 0x1408fd8a1
008FD9FE  83 E9 01                        sub ecx, 1
008FDA01  0F 84 9A FE FF FF               je 0x1408fd8a1
008FDA07  83 E9 01                        sub ecx, 1
008FDA0A  0F 84 91 FE FF FF               je 0x1408fd8a1
008FDA10  83 E9 01                        sub ecx, 1
008FDA13  0F 85 75 FE FF FF               jne 0x1408fd88e
008FDA19  BB 30 02 00 C0                  mov ebx, 0xc0000230
008FDA1E  E9 14 FF FF FF                  jmp 0x1408fd937
008FDA23  85 F6                           test esi, esi
008FDA25  0F 84 BC FE FF FF               je 0x1408fd8e7
008FDA2B  45 33 C0                        xor r8d, r8d
008FDA2E  8B D6                           mov edx, esi
008FDA30  48 8B CD                        mov rcx, rbp
008FDA33  E8 38 02 FC FF                  call 0x1408bdc70
008FDA38  84 C0                           test al, al
008FDA3A  0F 84 48 23 22 00               je 0x140b1fd88
008FDA40  48 8B CD                        mov rcx, rbp
008FDA43  E8 28 EE FB FF                  call 0x1408bc870
008FDA48  3B C6                           cmp eax, esi
008FDA4A  0F 84 97 FE FF FF               je 0x1408fd8e7
008FDA50  E9 33 23 22 00                  jmp 0x140b1fd88
008FDA55  BB 22 00 00 C0                  mov ebx, 0xc0000022
008FDA5A  E9 E6 FE FF FF                  jmp 0x1408fd945
008FDA5F  BB 30 02 00 C0                  mov ebx, 0xc0000230
008FDA64  E9 DC FE FF FF                  jmp 0x1408fd945
008FDA69  85 F6                           test esi, esi
008FDA6B  0F 84 76 FE FF FF               je 0x1408fd8e7
008FDA71  48 85 ED                        test rbp, rbp
008FDA74  0F 84 FE FE FF FF               je 0x1408fd978
008FDA7A  83 FE 04                        cmp esi, 4
008FDA7D  0F 85 F5 FE FF FF               jne 0x1408fd978
008FDA83  39 5D 00                        cmp dword ptr [rbp], ebx
008FDA86  0F 84 5B FE FF FF               je 0x1408fd8e7
008FDA8C  49 8B CF                        mov rcx, r15
008FDA8F  E8 50 4B 03 00                  call 0x1409325e4
008FDA94  84 C0                           test al, al
008FDA96  0F 84 4B FE FF FF               je 0x1408fd8e7
008FDA9C  BB 10 00 00 C0                  mov ebx, 0xc0000010
008FDAA1  E9 91 FE FF FF                  jmp 0x1408fd937
008FDAA6  83 FE 40                        cmp esi, 0x40
008FDAA9  0F 87 C9 FE FF FF               ja 0x1408fd978
008FDAAF  E9 33 FE FF FF                  jmp 0x1408fd8e7
008FDAB4  48 21 5C 24 38                  and qword ptr [rsp + 0x38], rbx
008FDAB9  48 8D 44 24 40                  lea rax, [rsp + 0x40]
008FDABE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008FDAC3  45 33 C9                        xor r9d, r9d
008FDAC6  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
008FDACA  49 8B D7                        mov rdx, r15
008FDACD  49 8B CC                        mov rcx, r12
008FDAD0  C7 44 24 20 02 00 00 02         mov dword ptr [rsp + 0x20], 0x2000002
008FDAD8  45 8D 41 10                     lea r8d, [r9 + 0x10]
008FDADC  E8 5F 0A FF FF                  call 0x1408ee540
008FDAE1  8B D8                           mov ebx, eax
008FDAE3  85 C0                           test eax, eax
008FDAE5  0F 88 4C FE FF FF               js 0x1408fd937
008FDAEB  E9 00 FE FF FF                  jmp 0x1408fd8f0
008FDAF0  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008FDAF5  0F 85 38 FE FF FF               jne 0x1408fd933
008FDAFB  E9 2E FE FF FF                  jmp 0x1408fd92e
008FDB00  E8 AB F7 DA FF                  call 0x1406ad2b0
008FDB05  E9 3B FE FF FF                  jmp 0x1408fd945
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _CmSetDeviceRegPropWorker(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7, unsigned __int16 a8)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (80);
    v_rbx = 0;
    if (a8 != 0) goto loc_008FD978;
    if ((unsigned int)((unsigned int)(a7)) != 0) goto loc_008FD967;
    v_rbp = 0;
loc_008FD854:
    if (((unsigned int)(a4 - 1)) > 36) goto loc_008FDA19;
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) <= 29) goto loc_008FD9DB;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4))))) - (30));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
loc_008FD88E:
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    if (((unsigned int)(a1)) != 1) goto loc_008FDA19;
loc_008FD8A1:
    result = _CmDevicePropertyWrite(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008FDA55;
    result = MapCmDevicePropertyToRegType((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_008FDA5F;
    if (a5 != ((unsigned int)(result))) goto loc_008FD978;
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) == 8) goto loc_008FDAA6;
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) == 11) goto loc_008FDA69;
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) == 24) goto loc_008FDA23;
loc_008FD8E7:
    if (a3 == 0) goto loc_008FDAB4;
loc_008FD8F0:
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) == 8) goto loc_008FD9AB;
    result = MapCmDevicePropertyToRegValue((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))), a3, a4);
    if (result == 0) goto loc_008FDA19;
    if ((unsigned int)((unsigned int)(a7)) != 0) goto loc_008FD97F;
    a2 = v_stack_m28;
    if (a3 != 0) { a2 = a3; }
    result = PnpCtxRegDeleteValue((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))), a2, result, a4);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_008FDAF0;
loc_008FD92E:
loc_008FD933:
    if (!sign_flag) goto loc_008FD9AB;
loc_008FD937:
    if (v_stack_m28 != 0) goto loc_008FDB00;
loc_008FD945:
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000225ULL)));
loc_008FD967:
    if (a6 != 0) goto loc_008FD854;
loc_008FD978:
    goto loc_008FD945;
loc_008FD97F:
    v_stack_m28 = (unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48));
    if (a3 != 0) { a2 = a3; }
    v_stack_m30 = a6;
    result = PnpCtxRegSetValue(v_stack_m28, a2, result, (unsigned int)(a5));
    if (((unsigned int)(result)) == 0xC000017CULL) goto loc_008FD9D1;
    if (!sign_flag) goto loc_008FD933;
    goto loc_008FD937;
loc_008FD9AB:
    v_stack_m30 = (unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 56));
    a4 = v_stack_m10;
    if (a3 != 0) { a4 = a3; }
    result = CmRaisePropertyChangeEvent(a1, a2, 1, a4);
    goto loc_008FD937;
loc_008FD9D1:
    goto loc_008FD937;
loc_008FD9DB:
    if (a3 == 0) goto loc_008FD8A1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 56)))) - (20));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_008FD88E;
loc_008FDA19:
    goto loc_008FD937;
loc_008FDA23:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48)) == 0) goto loc_008FD8E7;
    a3 = 0;
    result = RtlValidRelativeSecurityDescriptor(a6, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48))), a3, a4);
    result = RtlLengthSecurityDescriptor(a6, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48))), a3, a4);
    if (((unsigned int)(result)) == ((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48)))) goto loc_008FD8E7;
loc_008FDA55:
    goto loc_008FD945;
loc_008FDA5F:
    goto loc_008FD945;
loc_008FDA69:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48)) == 0) goto loc_008FD8E7;
    if (a6 == 0) goto loc_008FD978;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48))) != 4) goto loc_008FD978;
    if ((*(unsigned int *)(a6)) == ((unsigned int)((unsigned int)(0xC0000230ULL)))) goto loc_008FD8E7;
    result = CmIsRootDevice(a2, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008FD8E7;
    goto loc_008FD937;
loc_008FDAA6:
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 48))) > 64) goto loc_008FD978;
    goto loc_008FD8E7;
loc_008FDAB4:
    v_stack_m20 = v_stack_m10;
    a4 = 0;
    v_stack_m28 = (unsigned __int8)((unsigned int)(0xC0000010ULL));
    v_stack_m30 = 0x2000002ULL;
    result = _CmOpenDeviceRegKey(a1, a2, a4 + 16, a4);
    if (sign_flag) goto loc_008FD937;
    goto loc_008FD8F0;
loc_008FDAF0:
    if (((unsigned int)(result)) != 0xC000017CULL) goto loc_008FD933;
    goto loc_008FD92E;
loc_008FDB00:
    result = ZwClose(a1, a2, a4 + 16, a4);
    goto loc_008FD945;
}
```

## 5. (Beta) C Style

```c
int64_t _CmSetDeviceRegPropWorker(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, uint16_t Arg8)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (80);
    local_rbx = 0;
    if (Arg8 != 0) goto loc_008FD978;
    if ((uint32_t)((uint32_t)(Arg7)) != 0) goto loc_008FD967;
    local_rbp = 0;
loc_008FD854:
    if (((uint32_t)(Arg4 - 1)) > 36) goto loc_008FDA19;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) <= 29) goto loc_008FD9DB;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4))))) - (30));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
loc_008FD88E:
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    if (((uint32_t)(Arg1)) != 1) goto loc_008FDA19;
loc_008FD8A1:
    result = _CmDevicePropertyWrite(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008FDA55;
    result = MapCmDevicePropertyToRegType((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_008FDA5F;
    if (Arg5 != ((uint32_t)(result))) goto loc_008FD978;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) == 8) goto loc_008FDAA6;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) == 11) goto loc_008FDA69;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) == 24) goto loc_008FDA23;
loc_008FD8E7:
    if (Arg3 == 0) goto loc_008FDAB4;
loc_008FD8F0:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) == 8) goto loc_008FD9AB;
    result = MapCmDevicePropertyToRegValue((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))), Arg3, Arg4);
    if (result == 0) goto loc_008FDA19;
    if ((uint32_t)((uint32_t)(Arg7)) != 0) goto loc_008FD97F;
    Arg2 = v_stack_m28;
    if (Arg3 != 0) { Arg2 = Arg3; }
    result = PnpCtxRegDeleteValue((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))), Arg2, result, Arg4);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_008FDAF0;
loc_008FD92E:
loc_008FD933:
    if (!sign_flag) goto loc_008FD9AB;
loc_008FD937:
    if (v_stack_m28 != 0) goto loc_008FDB00;
loc_008FD945:
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000225ULL)));
loc_008FD967:
    if (Arg6 != 0) goto loc_008FD854;
loc_008FD978:
    goto loc_008FD945;
loc_008FD97F:
    v_stack_m28 = (uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30));
    if (Arg3 != 0) { Arg2 = Arg3; }
    v_stack_m30 = Arg6;
    result = PnpCtxRegSetValue(v_stack_m28, Arg2, result, (uint32_t)(Arg5));
    if (((uint32_t)(result)) == 0xC000017CULL) goto loc_008FD9D1;
    if (!sign_flag) goto loc_008FD933;
    goto loc_008FD937;
loc_008FD9AB:
    v_stack_m30 = (uint32_t)(*(uint64_t *)(v_stack_m18 + 0x38));
    Arg4 = v_stack_m10;
    if (Arg3 != 0) { Arg4 = Arg3; }
    result = CmRaisePropertyChangeEvent(Arg1, Arg2, 1, Arg4);
    goto loc_008FD937;
loc_008FD9D1:
    goto loc_008FD937;
loc_008FD9DB:
    if (Arg3 == 0) goto loc_008FD8A1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x38)))) - (20));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008FD8A1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_008FD88E;
loc_008FDA19:
    goto loc_008FD937;
loc_008FDA23:
    if ((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30)) == 0) goto loc_008FD8E7;
    Arg3 = 0;
    result = RtlValidRelativeSecurityDescriptor(Arg6, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30))), Arg3, Arg4);
    result = RtlLengthSecurityDescriptor(Arg6, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30))), Arg3, Arg4);
    if (((uint32_t)(result)) == ((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30)))) goto loc_008FD8E7;
loc_008FDA55:
    goto loc_008FD945;
loc_008FDA5F:
    goto loc_008FD945;
loc_008FDA69:
    if ((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30)) == 0) goto loc_008FD8E7;
    if (Arg6 == 0) goto loc_008FD978;
    if (((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30))) != 4) goto loc_008FD978;
    if ((*(uint32_t *)(Arg6)) == ((uint32_t)((uint32_t)(0xC0000230ULL)))) goto loc_008FD8E7;
    result = CmIsRootDevice(Arg2, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008FD8E7;
    goto loc_008FD937;
loc_008FDAA6:
    if (((uint32_t)(*(uint64_t *)(v_stack_m18 + 0x30))) > 64) goto loc_008FD978;
    goto loc_008FD8E7;
loc_008FDAB4:
    v_stack_m20 = v_stack_m10;
    Arg4 = 0;
    v_stack_m28 = (uint8_t)((uint32_t)(0xC0000010ULL));
    v_stack_m30 = 0x2000002ULL;
    result = _CmOpenDeviceRegKey(Arg1, Arg2, Arg4 + 16, Arg4);
    if (sign_flag) goto loc_008FD937;
    goto loc_008FD8F0;
loc_008FDAF0:
    if (((uint32_t)(result)) != 0xC000017CULL) goto loc_008FD933;
    goto loc_008FD92E;
loc_008FDB00:
    result = ZwClose(Arg1, Arg2, Arg4 + 16, Arg4);
    goto loc_008FD945;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FD804&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
