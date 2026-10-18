# TtmDispatchApi

- RVA: `0x0098AD08`–`0x0098AFAD` (길이 `677` bytes)
- VA: `0x000000014098AD08`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075C18`
- 디코드: `194`개 명령, `677/677` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0098AD2F` → [TtmiLogDispatchApiStart](TtmiLogDispatchApiStart_function_0098AFB4.md) (function, `0x0098AFB4`)
- `0x0098AD58` → [TtmIsEnabled](../91/TtmIsEnabled_function_009143D8.md) (function, `0x009143D8`)
- `0x0098AE00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0098AE7F` → [TtmpDispatchGetTerminalEvent](../77/TtmpDispatchGetTerminalEvent_function_007789F4.md) (function, `0x007789F4`)
- `0x0098AE8F` → [TtmpDispatchCreateEventQueue](../77/TtmpDispatchCreateEventQueue_function_00778718.md) (function, `0x00778718`)
- `0x0098AE9C` → [TtmpDispatchEvacuateDevices](../77/TtmpDispatchEvacuateDevices_function_00778948.md) (function, `0x00778948`)
- `0x0098AEAC` → [TtmpDispatchCreateTerminal](../77/TtmpDispatchCreateTerminal_function_00778858.md) (function, `0x00778858`)
- `0x0098AEBC` → [TtmpDispatchOpenTerminal](../77/TtmpDispatchOpenTerminal_function_00778AB8.md) (function, `0x00778AB8`)
- `0x0098AEC6` → [TtmpDispatchSetDefaultDeviceAssignment](../77/TtmpDispatchSetDefaultDeviceAssignment_function_00778B54.md) (function, `0x00778B54`)
- `0x0098AF03` → [TtmiLogError](TtmiLogError_function_0098B39C.md) (function, `0x0098B39C`)
- `0x0098AF0D` → [TtmpDispatchSetInputWakeCapability](../77/TtmpDispatchSetInputWakeCapability_function_00778E2C.md) (function, `0x00778E2C`)
- `0x0098AF17` → [TtmpDispatchSetDisplayPowerRequest](../77/TtmpDispatchSetDisplayPowerRequest_function_00778C10.md) (function, `0x00778C10`)
- `0x0098AF21` → [TtmpDispatchSetDisplayTimeouts](../77/TtmpDispatchSetDisplayTimeouts_function_00778D70.md) (function, `0x00778D70`)
- `0x0098AF2B` → [TtmpDispatchSetDisplayState](../77/TtmpDispatchSetDisplayState_function_00778CBC.md) (function, `0x00778CBC`)
- `0x0098AF35` → [TtmpDispatchAssignDevice](../77/TtmpDispatchAssignDevice_function_00778670.md) (function, `0x00778670`)
- `0x0098AF60` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0098AF7F` → [TtmiLogError](TtmiLogError_function_0098B39C.md) (function, `0x0098B39C`)
- `0x0098AF88` → [TtmiLogDispatchApiStop](TtmiLogDispatchApiStop_function_0098B084.md) (function, `0x0098B084`)

### Direct callers
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00957B47`

### Static image references
- `0x0098AEF0` → RVA `0x00B044B0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0098AE00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0098AF60` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098AD08  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0098AD0D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0098AD12  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0098AD17  57                              push rdi
0098AD18  41 54                           push r12
0098AD1A  41 55                           push r13
0098AD1C  41 56                           push r14
0098AD1E  41 57                           push r15
0098AD20  48 83 EC 20                     sub rsp, 0x20
0098AD24  4D 8B F1                        mov r14, r9
0098AD27  45 8B F8                        mov r15d, r8d
0098AD2A  48 8B FA                        mov rdi, rdx
0098AD2D  8B E9                           mov ebp, ecx
0098AD2F  E8 80 02 00 00                  call 0x14098afb4
0098AD34  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0098AD3C  33 F6                           xor esi, esi
0098AD3E  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
0098AD43  8B DE                           mov ebx, esi
0098AD45  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
0098AD4D  49 89 34 24                     mov qword ptr [r12], rsi
0098AD51  41 89 75 00                     mov dword ptr [r13], esi
0098AD55  40 88 30                        mov byte ptr [rax], sil
0098AD58  E8 7B 96 F8 FF                  call 0x1409143d8
0098AD5D  84 C0                           test al, al
0098AD5F  75 0F                           jne 0x14098ad70
0098AD61  BF BB 00 00 C0                  mov edi, 0xc00000bb
0098AD66  BA 21 04 00 00                  mov edx, 0x421
0098AD6B  E9 01 02 00 00                  jmp 0x14098af71
0098AD70  BA 05 10 00 00                  mov edx, 0x1005
0098AD75  3B EA                           cmp ebp, edx
0098AD77  0F 8F A6 00 00 00               jg 0x14098ae23
0098AD7D  74 48                           je 0x14098adc7
0098AD7F  8B CD                           mov ecx, ebp
0098AD81  81 E9 00 10 00 00               sub ecx, 0x1000
0098AD87  0F 84 8F 00 00 00               je 0x14098ae1c
0098AD8D  83 E9 01                        sub ecx, 1
0098AD90  74 30                           je 0x14098adc2
0098AD92  83 E9 01                        sub ecx, 1
0098AD95  74 24                           je 0x14098adbb
0098AD97  83 E9 01                        sub ecx, 1
0098AD9A  74 13                           je 0x14098adaf
0098AD9C  83 F9 01                        cmp ecx, 1
0098AD9F  0F 85 9C 00 00 00               jne 0x14098ae41
0098ADA5  8D 41 0F                        lea eax, [rcx + 0xf]
0098ADA8  BE 20 02 00 00                  mov esi, 0x220
0098ADAD  EB 1D                           jmp 0x14098adcc
0098ADAF  B8 10 00 00 00                  mov eax, 0x10
0098ADB4  BE 08 00 00 00                  mov esi, 8
0098ADB9  EB 11                           jmp 0x14098adcc
0098ADBB  B8 10 00 00 00                  mov eax, 0x10
0098ADC0  EB 0A                           jmp 0x14098adcc
0098ADC2  BE 10 00 00 00                  mov esi, 0x10
0098ADC7  B8 18 00 00 00                  mov eax, 0x18
0098ADCC  44 3B F8                        cmp r15d, eax
0098ADCF  0F 82 92 01 00 00               jb 0x14098af67
0098ADD5  4D 85 F6                        test r14, r14
0098ADD8  75 08                           jne 0x14098ade2
0098ADDA  85 F6                           test esi, esi
0098ADDC  0F 85 85 01 00 00               jne 0x14098af67
0098ADE2  39 74 24 70                     cmp dword ptr [rsp + 0x70], esi
0098ADE6  0F 82 7B 01 00 00               jb 0x14098af67
0098ADEC  41 BE 4D 65 6D 20               mov r14d, 0x206d654d
0098ADF2  85 F6                           test esi, esi
0098ADF4  74 5F                           je 0x14098ae55
0098ADF6  8B D6                           mov edx, esi
0098ADF8  45 8B C6                        mov r8d, r14d
0098ADFB  B9 00 01 00 00                  mov ecx, 0x100
0098AE00  E8 EB 72 1F 00                  call 0x140b820f0
0098AE05  48 8B D8                        mov rbx, rax
0098AE08  48 85 C0                        test rax, rax
0098AE0B  75 43                           jne 0x14098ae50
0098AE0D  BF 17 00 00 C0                  mov edi, 0xc0000017
0098AE12  BA 7D 04 00 00                  mov edx, 0x47d
0098AE17  E9 55 01 00 00                  jmp 0x14098af71
0098AE1C  B8 0C 00 00 00                  mov eax, 0xc
0098AE21  EB 91                           jmp 0x14098adb4
0098AE23  8B CD                           mov ecx, ebp
0098AE25  81 E9 06 10 00 00               sub ecx, 0x1006
0098AE2B  74 9A                           je 0x14098adc7
0098AE2D  83 E9 01                        sub ecx, 1
0098AE30  74 95                           je 0x14098adc7
0098AE32  83 E9 01                        sub ecx, 1
0098AE35  74 90                           je 0x14098adc7
0098AE37  83 E9 01                        sub ecx, 1
0098AE3A  74 8B                           je 0x14098adc7
0098AE3C  83 F9 01                        cmp ecx, 1
0098AE3F  74 86                           je 0x14098adc7
0098AE41  BF 0D 00 00 C0                  mov edi, 0xc000000d
0098AE46  BA 63 04 00 00                  mov edx, 0x463
0098AE4B  E9 21 01 00 00                  jmp 0x14098af71
0098AE50  BA 05 10 00 00                  mov edx, 0x1005
0098AE55  3B EA                           cmp ebp, edx
0098AE57  7F 74                           jg 0x14098aecd
0098AE59  74 68                           je 0x14098aec3
0098AE5B  8B CD                           mov ecx, ebp
0098AE5D  81 E9 00 10 00 00               sub ecx, 0x1000
0098AE63  74 51                           je 0x14098aeb6
0098AE65  83 E9 01                        sub ecx, 1
0098AE68  74 3C                           je 0x14098aea6
0098AE6A  83 E9 01                        sub ecx, 1
0098AE6D  74 2A                           je 0x14098ae99
0098AE6F  83 E9 01                        sub ecx, 1
0098AE72  74 15                           je 0x14098ae89
0098AE74  83 F9 01                        cmp ecx, 1
0098AE77  75 72                           jne 0x14098aeeb
0098AE79  48 8B D3                        mov rdx, rbx
0098AE7C  48 8B CF                        mov rcx, rdi
0098AE7F  E8 70 DB DE FF                  call 0x1407789f4
0098AE84  E9 B1 00 00 00                  jmp 0x14098af3a
0098AE89  48 8B D3                        mov rdx, rbx
0098AE8C  48 8B CF                        mov rcx, rdi
0098AE8F  E8 84 D8 DE FF                  call 0x140778718
0098AE94  E9 A1 00 00 00                  jmp 0x14098af3a
0098AE99  48 8B CF                        mov rcx, rdi
0098AE9C  E8 A7 DA DE FF                  call 0x140778948
0098AEA1  E9 94 00 00 00                  jmp 0x14098af3a
0098AEA6  48 8B D3                        mov rdx, rbx
0098AEA9  48 8B CF                        mov rcx, rdi
0098AEAC  E8 A7 D9 DE FF                  call 0x140778858
0098AEB1  E9 84 00 00 00                  jmp 0x14098af3a
0098AEB6  48 8B D3                        mov rdx, rbx
0098AEB9  48 8B CF                        mov rcx, rdi
0098AEBC  E8 F7 DB DE FF                  call 0x140778ab8
0098AEC1  EB 77                           jmp 0x14098af3a
0098AEC3  48 8B CF                        mov rcx, rdi
0098AEC6  E8 89 DC DE FF                  call 0x140778b54
0098AECB  EB 6D                           jmp 0x14098af3a
0098AECD  8B CD                           mov ecx, ebp
0098AECF  81 E9 06 10 00 00               sub ecx, 0x1006
0098AED5  74 5B                           je 0x14098af32
0098AED7  83 E9 01                        sub ecx, 1
0098AEDA  74 4C                           je 0x14098af28
0098AEDC  83 E9 01                        sub ecx, 1
0098AEDF  74 3D                           je 0x14098af1e
0098AEE1  83 E9 01                        sub ecx, 1
0098AEE4  74 2E                           je 0x14098af14
0098AEE6  83 F9 01                        cmp ecx, 1
0098AEE9  74 1F                           je 0x14098af0a
0098AEEB  BF 0D 00 00 C0                  mov edi, 0xc000000d
0098AEF0  48 8D 0D B9 95 17 00            lea rcx, [rip + 0x1795b9]
0098AEF7  44 8B CF                        mov r9d, edi
0098AEFA  41 83 C8 FF                     or r8d, 0xffffffff
0098AEFE  BA C2 04 00 00                  mov edx, 0x4c2
0098AF03  E8 94 04 00 00                  call 0x14098b39c
0098AF08  EB 32                           jmp 0x14098af3c
0098AF0A  48 8B CF                        mov rcx, rdi
0098AF0D  E8 1A DF DE FF                  call 0x140778e2c
0098AF12  EB 26                           jmp 0x14098af3a
0098AF14  48 8B CF                        mov rcx, rdi
0098AF17  E8 F4 DC DE FF                  call 0x140778c10
0098AF1C  EB 1C                           jmp 0x14098af3a
0098AF1E  48 8B CF                        mov rcx, rdi
0098AF21  E8 4A DE DE FF                  call 0x140778d70
0098AF26  EB 12                           jmp 0x14098af3a
0098AF28  48 8B CF                        mov rcx, rdi
0098AF2B  E8 8C DD DE FF                  call 0x140778cbc
0098AF30  EB 08                           jmp 0x14098af3a
0098AF32  48 8B CF                        mov rcx, rdi
0098AF35  E8 36 D7 DE FF                  call 0x140778670
0098AF3A  8B F8                           mov edi, eax
0098AF3C  48 85 DB                        test rbx, rbx
0098AF3F  74 43                           je 0x14098af84
0098AF41  85 FF                           test edi, edi
0098AF43  78 15                           js 0x14098af5a
0098AF45  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0098AF4D  49 89 1C 24                     mov qword ptr [r12], rbx
0098AF51  41 89 75 00                     mov dword ptr [r13], esi
0098AF55  C6 00 01                        mov byte ptr [rax], 1
0098AF58  EB 2A                           jmp 0x14098af84
0098AF5A  41 8B D6                        mov edx, r14d
0098AF5D  48 8B CB                        mov rcx, rbx
0098AF60  E8 0B 79 1F 00                  call 0x140b82870
0098AF65  EB 1D                           jmp 0x14098af84
0098AF67  BF 23 00 00 C0                  mov edi, 0xc0000023
0098AF6C  BA 6E 04 00 00                  mov edx, 0x46e
0098AF71  44 8B CF                        mov r9d, edi
0098AF74  48 8D 0D 35 95 17 00            lea rcx, [rip + 0x179535]
0098AF7B  41 83 C8 FF                     or r8d, 0xffffffff
0098AF7F  E8 18 04 00 00                  call 0x14098b39c
0098AF84  8B D7                           mov edx, edi
0098AF86  8B CD                           mov ecx, ebp
0098AF88  E8 F7 00 00 00                  call 0x14098b084
0098AF8D  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0098AF92  8B C7                           mov eax, edi
0098AF94  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0098AF99  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0098AF9E  48 83 C4 20                     add rsp, 0x20
0098AFA2  41 5F                           pop r15
0098AFA4  41 5E                           pop r14
0098AFA6  41 5D                           pop r13
0098AFA8  41 5C                           pop r12
0098AFAA  5F                              pop rdi
0098AFAB  C3                              ret
0098AFAC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmDispatchApi(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = TtmiLogDispatchApiStart(a1, a2, a3, a4);
    v_rsi = 0;
    *(unsigned __int64 *)(a6) = 0;
    *(unsigned int *)(a7) = 0;
    *(unsigned __int8 *)(a8) = 0;
    result = TtmIsEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0098AD70;
    goto loc_0098AF71;
loc_0098AD70:
    if (((unsigned int)((unsigned int)(a1))) > ((unsigned int)((unsigned int)(0x1005ULL)))) goto loc_0098AE23;
    if (((unsigned int)((unsigned int)(a1))) == ((unsigned int)((unsigned int)(0x1005ULL)))) goto loc_0098ADC7;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (0x1000ULL));
    if (condition_is_equal) goto loc_0098AE1C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098ADC2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098ADBB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098ADAF;
    if (a1 != 1) goto loc_0098AE41;
    goto loc_0098ADCC;
loc_0098ADAF:
loc_0098ADB4:
    goto loc_0098ADCC;
loc_0098ADBB:
    goto loc_0098ADCC;
loc_0098ADC2:
loc_0098ADC7:
loc_0098ADCC:
    if (((unsigned int)((unsigned int)(a3))) < 24) goto loc_0098AF67;
    if (a4 != 0) goto loc_0098ADE2;
    if (16 != 0) goto loc_0098AF67;
loc_0098ADE2:
    if (a5 < 16) goto loc_0098AF67;
    if (16 == 0) goto loc_0098AE55;
    result = ExAllocatePool2(256, 16, (unsigned int)((unsigned int)((unsigned int)(0x206D654DULL))), a4);
    if (result != 0) goto loc_0098AE50;
    goto loc_0098AF71;
loc_0098AE1C:
    goto loc_0098ADB4;
loc_0098AE23:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (0x1006ULL));
    if (condition_is_equal) goto loc_0098ADC7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098ADC7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098ADC7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098ADC7;
    if (a1 == 1) goto loc_0098ADC7;
loc_0098AE41:
    goto loc_0098AF71;
loc_0098AE50:
loc_0098AE55:
    if (((unsigned int)((unsigned int)(a1))) > ((unsigned int)((unsigned int)(0x1005ULL)))) goto loc_0098AECD;
    if (((unsigned int)((unsigned int)(a1))) == ((unsigned int)((unsigned int)(0x1005ULL)))) goto loc_0098AEC3;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (0x1000ULL));
    if (condition_is_equal) goto loc_0098AEB6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098AEA6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098AE99;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098AE89;
    if (a1 != 1) goto loc_0098AEEB;
    result = TtmpDispatchGetTerminalEvent((unsigned int)(0xC000000DULL), result, (unsigned int)((unsigned int)((unsigned int)(0x206D654DULL))), a4);
    goto loc_0098AF3A;
loc_0098AE89:
    result = TtmpDispatchCreateEventQueue((unsigned int)(0xC000000DULL), result, (unsigned int)((unsigned int)((unsigned int)(0x206D654DULL))), a4);
    goto loc_0098AF3A;
loc_0098AE99:
    result = TtmpDispatchEvacuateDevices((unsigned int)(0xC000000DULL), result, (unsigned int)((unsigned int)((unsigned int)(0x206D654DULL))), a4);
    goto loc_0098AF3A;
loc_0098AEA6:
    result = TtmpDispatchCreateTerminal((unsigned int)(0xC000000DULL), result, (unsigned int)((unsigned int)((unsigned int)(0x206D654DULL))), a4);
    goto loc_0098AF3A;
loc_0098AEB6:
    result = TtmpDispatchOpenTerminal((unsigned int)(0xC000000DULL), result, (unsigned int)((unsigned int)((unsigned int)(0x206D654DULL))), a4);
    goto loc_0098AF3A;
loc_0098AEC3:
    result = TtmpDispatchSetDefaultDeviceAssignment((unsigned int)(0xC000000DULL), result, (unsigned int)((unsigned int)((unsigned int)(0x206D654DULL))), a4);
    goto loc_0098AF3A;
loc_0098AECD:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (0x1006ULL));
    if (condition_is_equal) goto loc_0098AF32;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098AF28;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098AF1E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0098AF14;
    if (a1 == 1) goto loc_0098AF0A;
loc_0098AEEB:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x206D654DULL)))) | (0xFFFFFFFFULL));
    result = TtmiLogError(v_rip + 1545657, (unsigned int)(0x4C2ULL), a3, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    goto loc_0098AF3C;
loc_0098AF0A:
    result = TtmpDispatchSetInputWakeCapability((unsigned int)(0xC000000DULL), (unsigned int)(0x4C2ULL), a3, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    goto loc_0098AF3A;
loc_0098AF14:
    result = TtmpDispatchSetDisplayPowerRequest((unsigned int)(0xC000000DULL), (unsigned int)(0x4C2ULL), a3, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    goto loc_0098AF3A;
loc_0098AF1E:
    result = TtmpDispatchSetDisplayTimeouts((unsigned int)(0xC000000DULL), (unsigned int)(0x4C2ULL), a3, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    goto loc_0098AF3A;
loc_0098AF28:
    result = TtmpDispatchSetDisplayState((unsigned int)(0xC000000DULL), (unsigned int)(0x4C2ULL), a3, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    goto loc_0098AF3A;
loc_0098AF32:
    result = TtmpDispatchAssignDevice((unsigned int)(0xC000000DULL), (unsigned int)(0x4C2ULL), a3, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
loc_0098AF3A:
loc_0098AF3C:
    if (result == 0) goto loc_0098AF84;
    if (sign_flag) goto loc_0098AF5A;
    *(unsigned __int64 *)(a6) = result;
    *(unsigned int *)(a7) = 16;
    *(unsigned __int8 *)(a8) = 1;
    goto loc_0098AF84;
loc_0098AF5A:
    result = ExFreePoolWithTag(result, (unsigned int)((unsigned int)((unsigned int)(0x206D654DULL))), a3, (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
    goto loc_0098AF84;
loc_0098AF67:
loc_0098AF71:
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    result = TtmiLogError(v_rip + 1545525, (unsigned int)(0x46EULL), a3, (unsigned int)((unsigned int)((unsigned int)(0xC0000023ULL))));
loc_0098AF84:
    result = TtmiLogDispatchApiStop((unsigned int)((unsigned int)((unsigned int)(a1))), (unsigned int)((unsigned int)((unsigned int)(0xC0000023ULL))), a3, (unsigned int)((unsigned int)((unsigned int)(0xC0000023ULL))));
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000023ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t TtmDispatchApi(int32_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, void *Arg6, void *Arg7, void *Arg8)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = TtmiLogDispatchApiStart(Arg1, Arg2, Arg3, Arg4);
    local_rsi = 0;
    *(uint64_t *)(arg6) = 0;
    *(uint32_t *)(arg7) = 0;
    *(uint8_t *)(arg8) = 0;
    result = TtmIsEnabled(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0098AD70;
    goto loc_0098AF71;
loc_0098AD70:
    if (((uint32_t)((uint32_t)(Arg1))) > ((uint32_t)((uint32_t)(0x1005ULL)))) goto loc_0098AE23;
    if (((uint32_t)((uint32_t)(Arg1))) == ((uint32_t)((uint32_t)(0x1005ULL)))) goto loc_0098ADC7;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (0x1000ULL));
    if (condition_is_equal) goto loc_0098AE1C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098ADC2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098ADBB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098ADAF;
    if (Arg1 != 1) goto loc_0098AE41;
    goto loc_0098ADCC;
loc_0098ADAF:
loc_0098ADB4:
    goto loc_0098ADCC;
loc_0098ADBB:
    goto loc_0098ADCC;
loc_0098ADC2:
loc_0098ADC7:
loc_0098ADCC:
    if (((uint32_t)((uint32_t)(Arg3))) < 24) goto loc_0098AF67;
    if (Arg4 != 0) goto loc_0098ADE2;
    if (16 != 0) goto loc_0098AF67;
loc_0098ADE2:
    if (Arg5 < 16) goto loc_0098AF67;
    if (16 == 0) goto loc_0098AE55;
    result = ExAllocatePool2(256, 16, (uint32_t)((uint32_t)((uint32_t)(0x206D654DULL))), Arg4);
    if (result != 0) goto loc_0098AE50;
    goto loc_0098AF71;
loc_0098AE1C:
    goto loc_0098ADB4;
loc_0098AE23:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (0x1006ULL));
    if (condition_is_equal) goto loc_0098ADC7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098ADC7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098ADC7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098ADC7;
    if (Arg1 == 1) goto loc_0098ADC7;
loc_0098AE41:
    goto loc_0098AF71;
loc_0098AE50:
loc_0098AE55:
    if (((uint32_t)((uint32_t)(Arg1))) > ((uint32_t)((uint32_t)(0x1005ULL)))) goto loc_0098AECD;
    if (((uint32_t)((uint32_t)(Arg1))) == ((uint32_t)((uint32_t)(0x1005ULL)))) goto loc_0098AEC3;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (0x1000ULL));
    if (condition_is_equal) goto loc_0098AEB6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098AEA6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098AE99;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098AE89;
    if (Arg1 != 1) goto loc_0098AEEB;
    result = TtmpDispatchGetTerminalEvent((uint32_t)(0xC000000DULL), result, (uint32_t)((uint32_t)((uint32_t)(0x206D654DULL))), Arg4);
    goto loc_0098AF3A;
loc_0098AE89:
    result = TtmpDispatchCreateEventQueue((uint32_t)(0xC000000DULL), result, (uint32_t)((uint32_t)((uint32_t)(0x206D654DULL))), Arg4);
    goto loc_0098AF3A;
loc_0098AE99:
    result = TtmpDispatchEvacuateDevices((uint32_t)(0xC000000DULL), result, (uint32_t)((uint32_t)((uint32_t)(0x206D654DULL))), Arg4);
    goto loc_0098AF3A;
loc_0098AEA6:
    result = TtmpDispatchCreateTerminal((uint32_t)(0xC000000DULL), result, (uint32_t)((uint32_t)((uint32_t)(0x206D654DULL))), Arg4);
    goto loc_0098AF3A;
loc_0098AEB6:
    result = TtmpDispatchOpenTerminal((uint32_t)(0xC000000DULL), result, (uint32_t)((uint32_t)((uint32_t)(0x206D654DULL))), Arg4);
    goto loc_0098AF3A;
loc_0098AEC3:
    result = TtmpDispatchSetDefaultDeviceAssignment((uint32_t)(0xC000000DULL), result, (uint32_t)((uint32_t)((uint32_t)(0x206D654DULL))), Arg4);
    goto loc_0098AF3A;
loc_0098AECD:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (0x1006ULL));
    if (condition_is_equal) goto loc_0098AF32;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098AF28;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098AF1E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0098AF14;
    if (Arg1 == 1) goto loc_0098AF0A;
loc_0098AEEB:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x206D654DULL)))) | (0xFFFFFFFFULL));
    result = TtmiLogError(v_rip + 1545657, (uint32_t)(0x4C2ULL), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    goto loc_0098AF3C;
loc_0098AF0A:
    result = TtmpDispatchSetInputWakeCapability((uint32_t)(0xC000000DULL), (uint32_t)(0x4C2ULL), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    goto loc_0098AF3A;
loc_0098AF14:
    result = TtmpDispatchSetDisplayPowerRequest((uint32_t)(0xC000000DULL), (uint32_t)(0x4C2ULL), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    goto loc_0098AF3A;
loc_0098AF1E:
    result = TtmpDispatchSetDisplayTimeouts((uint32_t)(0xC000000DULL), (uint32_t)(0x4C2ULL), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    goto loc_0098AF3A;
loc_0098AF28:
    result = TtmpDispatchSetDisplayState((uint32_t)(0xC000000DULL), (uint32_t)(0x4C2ULL), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    goto loc_0098AF3A;
loc_0098AF32:
    result = TtmpDispatchAssignDevice((uint32_t)(0xC000000DULL), (uint32_t)(0x4C2ULL), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
loc_0098AF3A:
loc_0098AF3C:
    if (result == 0) goto loc_0098AF84;
    if (sign_flag) goto loc_0098AF5A;
    *(uint64_t *)(arg6) = result;
    *(uint32_t *)(arg7) = 16;
    *(uint8_t *)(arg8) = 1;
    goto loc_0098AF84;
loc_0098AF5A:
    result = ExFreePoolWithTag(result, (uint32_t)((uint32_t)((uint32_t)(0x206D654DULL))), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
    goto loc_0098AF84;
loc_0098AF67:
loc_0098AF71:
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    result = TtmiLogError(v_rip + 1545525, (uint32_t)(0x46EULL), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC0000023ULL))));
loc_0098AF84:
    result = TtmiLogDispatchApiStop((uint32_t)((uint32_t)((uint32_t)(Arg1))), (uint32_t)((uint32_t)((uint32_t)(0xC0000023ULL))), Arg3, (uint32_t)((uint32_t)((uint32_t)(0xC0000023ULL))));
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000023ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `W` |
| `Arg7` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098AD08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
