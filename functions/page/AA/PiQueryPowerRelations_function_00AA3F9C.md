# PiQueryPowerRelations

- RVA: `0x00AA3F9C`–`0x00AA451B` (길이 `1,407` bytes)
- VA: `0x0000000140AA3F9C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB508`
- 디코드: `355`개 명령, `1,407/1,407` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AA3FED` → [PnpQueryDeviceRelations](../8F/PnpQueryDeviceRelations_function_008F9FE0.md) (function, `0x008F9FE0`)
- `0x00AA4001` → [PnpAcquirePowerRelationsQueueLock](../../text/4B/PnpAcquirePowerRelationsQueueLock_function_004B9534.md) (function, `0x004B9534`)
- `0x00AA4064` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA406E` → [PnpReleasePowerRelationsQueueLock](../../text/4B/PnpReleasePowerRelationsQueueLock_function_004BE70C.md) (function, `0x004BE70C`)
- `0x00AA40DF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA4105` → [PnpAcquirePowerRelationsQueueLock](../../text/4B/PnpAcquirePowerRelationsQueueLock_function_004B9534.md) (function, `0x004B9534`)
- `0x00AA4143` → [PnpReleasePowerRelationsQueueLock](../../text/4B/PnpReleasePowerRelationsQueueLock_function_004BE70C.md) (function, `0x004BE70C`)
- `0x00AA4175` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA419D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA41CE` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA41E8` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA4262` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA4276` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA4283` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA42E5` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA433D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA43D4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA4433` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00AA4452` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00AA445D` → [PiQueryPowerDependencyRelations](PiQueryPowerDependencyRelations_function_00AA4524.md) (function, `0x00AA4524`)
- `0x00AA446E` → [PiValidatePowerRelations](PiValidatePowerRelations_function_00AA4768.md) (function, `0x00AA4768`)
- `0x00AA4487` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AA449B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA44BA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AA44E5` → [PiPnpRtlPdoRaiseNtPlugPlayPropertyChangeEvent](../AB/PiPnpRtlPdoRaiseNtPlugPlayPropertyChangeEvent_function_00AB447C.md) (function, `0x00AB447C`)
- `0x00AA44F1` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AA44F6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [sub_006F45AA](../../text/6F/Unknown_function_006F45AA.md) at `0x006F4630`
- [PipProcessRebuildPowerRelationsQueue](../A0/PipProcessRebuildPowerRelationsQueue_function_00A06844.md) at `0x00A06908`

### Static image references
- `0x00AA44A9` → RVA `0x00F8C560` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x00AA4001` → [PnpAcquirePowerRelationsQueueLock](../../text/4B/PnpAcquirePowerRelationsQueueLock_function_004B9534.md) (`PAGE` → `.text`)
  - `0x00AA4064` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA406E` → [PnpReleasePowerRelationsQueueLock](../../text/4B/PnpReleasePowerRelationsQueueLock_function_004BE70C.md) (`PAGE` → `.text`)
  - `0x00AA40DF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA4105` → [PnpAcquirePowerRelationsQueueLock](../../text/4B/PnpAcquirePowerRelationsQueueLock_function_004B9534.md) (`PAGE` → `.text`)
  - `0x00AA4143` → [PnpReleasePowerRelationsQueueLock](../../text/4B/PnpReleasePowerRelationsQueueLock_function_004BE70C.md) (`PAGE` → `.text`)
  - `0x00AA4175` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA419D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA41CE` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA41E8` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA4262` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA4276` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA4283` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA42E5` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA433D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA43D4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA4433` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00AA4452` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00AA4487` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AA449B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA44BA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AA44F1` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AA44F6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA3F9C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00AA3FA1  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00AA3FA6  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00AA3FAB  55                              push rbp
00AA3FAC  41 54                           push r12
00AA3FAE  41 55                           push r13
00AA3FB0  41 56                           push r14
00AA3FB2  41 57                           push r15
00AA3FB4  48 8B EC                        mov rbp, rsp
00AA3FB7  48 83 EC 30                     sub rsp, 0x30
00AA3FBB  33 DB                           xor ebx, ebx
00AA3FBD  4C 8B F1                        mov r14, rcx
00AA3FC0  8B F3                           mov esi, ebx
00AA3FC2  48 89 5D 30                     mov qword ptr [rbp + 0x30], rbx
00AA3FC6  48 39 59 10                     cmp qword ptr [rcx + 0x10], rbx
00AA3FCA  75 0A                           jne 0x140aa3fd6
00AA3FCC  B8 89 01 00 C0                  mov eax, 0xc0000189
00AA3FD1  E9 27 05 00 00                  jmp 0x140aa44fd
00AA3FD6  84 D2                           test dl, dl
00AA3FD8  0F 85 7C 04 00 00               jne 0x140aa445a
00AA3FDE  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00AA3FE2  4C 8D 4D 30                     lea r9, [rbp + 0x30]
00AA3FE6  45 33 C0                        xor r8d, r8d
00AA3FE9  41 8D 50 02                     lea edx, [r8 + 2]
00AA3FED  E8 EE 5F E5 FF                  call 0x1408f9fe0
00AA3FF2  8B F0                           mov esi, eax
00AA3FF4  85 C0                           test eax, eax
00AA3FF6  79 09                           jns 0x140aa4001
00AA3FF8  48 89 5D 30                     mov qword ptr [rbp + 0x30], rbx
00AA3FFC  E9 59 04 00 00                  jmp 0x140aa445a
00AA4001  E8 2E 55 A1 FF                  call 0x1404b9534
00AA4006  4D 8D AE C0 00 00 00            lea r13, [r14 + 0xc0]
00AA400D  49 8B 7D 00                     mov rdi, qword ptr [r13]
00AA4011  EB 56                           jmp 0x140aa4069
00AA4013  48 8B 07                        mov rax, qword ptr [rdi]
00AA4016  48 8B CF                        mov rcx, rdi
00AA4019  48 8B F8                        mov rdi, rax
00AA401C  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00AA4020  0F 85 2E 01 00 00               jne 0x140aa4154
00AA4026  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00AA402A  48 39 0A                        cmp qword ptr [rdx], rcx
00AA402D  0F 85 21 01 00 00               jne 0x140aa4154
00AA4033  48 89 02                        mov qword ptr [rdx], rax
00AA4036  48 89 50 08                     mov qword ptr [rax + 8], rdx
00AA403A  48 8D 41 18                     lea rax, [rcx + 0x18]
00AA403E  4C 8B 00                        mov r8, qword ptr [rax]
00AA4041  49 39 40 08                     cmp qword ptr [r8 + 8], rax
00AA4045  0F 85 09 01 00 00               jne 0x140aa4154
00AA404B  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00AA404F  48 39 02                        cmp qword ptr [rdx], rax
00AA4052  0F 85 FC 00 00 00               jne 0x140aa4154
00AA4058  4C 89 02                        mov qword ptr [rdx], r8
00AA405B  49 89 50 08                     mov qword ptr [r8 + 8], rdx
00AA405F  BA 44 50 77 72                  mov edx, 0x72775044
00AA4064  E8 07 E8 0D 00                  call 0x140b82870
00AA4069  49 3B FD                        cmp rdi, r13
00AA406C  75 A5                           jne 0x140aa4013
00AA406E  E8 99 A6 A1 FF                  call 0x1404be70c
00AA4073  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA4077  4D 85 C0                        test r8, r8
00AA407A  0F 84 D8 03 00 00               je 0x140aa4458
00AA4080  41 39 18                        cmp dword ptr [r8], ebx
00AA4083  0F 84 CF 03 00 00               je 0x140aa4458
00AA4089  44 8B E3                        mov r12d, ebx
00AA408C  45 3B 20                        cmp r12d, dword ptr [r8]
00AA408F  0F 83 C5 03 00 00               jae 0x140aa445a
00AA4095  41 8B FC                        mov edi, r12d
00AA4098  49 8B 44 F8 08                  mov rax, qword ptr [r8 + rdi*8 + 8]
00AA409D  48 85 C0                        test rax, rax
00AA40A0  0F 84 96 03 00 00               je 0x140aa443c
00AA40A6  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00AA40AD  4C 8B 78 28                     mov r15, qword ptr [rax + 0x28]
00AA40B1  4D 85 FF                        test r15, r15
00AA40B4  0F 84 AB 00 00 00               je 0x140aa4165
00AA40BA  41 F7 87 8C 01 00 00 00 00 02 00  test dword ptr [r15 + 0x18c], 0x20000
00AA40C5  0F 85 9A 00 00 00               jne 0x140aa4165
00AA40CB  49 39 5F 10                     cmp qword ptr [r15 + 0x10], rbx
00AA40CF  74 7B                           je 0x140aa414c
00AA40D1  BA 38 00 00 00                  mov edx, 0x38
00AA40D6  41 B8 44 50 77 72               mov r8d, 0x72775044
00AA40DC  8D 4A 08                        lea ecx, [rdx + 8]
00AA40DF  E8 0C E0 0D 00                  call 0x140b820f0
00AA40E4  48 8B F8                        mov rdi, rax
00AA40E7  48 85 C0                        test rax, rax
00AA40EA  74 6F                           je 0x140aa415b
00AA40EC  88 58 30                        mov byte ptr [rax + 0x30], bl
00AA40EF  49 8D 8F A0 00 00 00            lea rcx, [r15 + 0xa0]
00AA40F6  49 8D 86 A0 00 00 00            lea rax, [r14 + 0xa0]
00AA40FD  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
00AA4101  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00AA4105  E8 2A 54 A1 FF                  call 0x1404b9534
00AA410A  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00AA410E  4C 39 28                        cmp qword ptr [rax], r13
00AA4111  75 41                           jne 0x140aa4154
00AA4113  4C 89 2F                        mov qword ptr [rdi], r13
00AA4116  49 81 C7 B0 00 00 00            add r15, 0xb0
00AA411D  48 89 47 08                     mov qword ptr [rdi + 8], rax
00AA4121  48 89 38                        mov qword ptr [rax], rdi
00AA4124  49 89 7D 08                     mov qword ptr [r13 + 8], rdi
00AA4128  48 83 C7 18                     add rdi, 0x18
00AA412C  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00AA4130  4C 39 38                        cmp qword ptr [rax], r15
00AA4133  75 1F                           jne 0x140aa4154
00AA4135  4C 89 3F                        mov qword ptr [rdi], r15
00AA4138  48 89 47 08                     mov qword ptr [rdi + 8], rax
00AA413C  48 89 38                        mov qword ptr [rax], rdi
00AA413F  49 89 7F 08                     mov qword ptr [r15 + 8], rdi
00AA4143  E8 C4 A5 A1 FF                  call 0x1404be70c
00AA4148  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA414C  41 FF C4                        inc r12d
00AA414F  E9 38 FF FF FF                  jmp 0x140aa408c
00AA4154  B9 03 00 00 00                  mov ecx, 3
00AA4159  CD 29                           int 0x29
00AA415B  BE 9A 00 00 C0                  mov esi, 0xc000009a
00AA4160  E9 F5 02 00 00                  jmp 0x140aa445a
00AA4165  0F AE E8                        lfence
00AA4168  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA416C  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA4171  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00AA4175  E8 FA 41 98 FF                  call 0x140428374
00AA417A  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA417E  49 8B 44 F8 08                  mov rax, qword ptr [r8 + rdi*8 + 8]
00AA4183  48 39 58 08                     cmp qword ptr [rax + 8], rbx
00AA4187  74 68                           je 0x140aa41f1
00AA4189  0F AE E8                        lfence
00AA418C  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA4190  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA4195  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AA4199  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
00AA419D  E8 D2 41 98 FF                  call 0x140428374
00AA41A2  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA41A6  49 8B 44 F8 08                  mov rax, qword ptr [r8 + rdi*8 + 8]
00AA41AB  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AA41AF  66 39 59 38                     cmp word ptr [rcx + 0x38], bx
00AA41B3  74 3C                           je 0x140aa41f1
00AA41B5  0F AE E8                        lfence
00AA41B8  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA41BC  BA 02 00 00 00                  mov edx, 2
00AA41C1  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA41C6  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AA41CA  48 83 C1 38                     add rcx, 0x38
00AA41CE  E8 A1 41 98 FF                  call 0x140428374
00AA41D3  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA41D7  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA41DC  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AA41E0  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00AA41E4  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00AA41E8  E8 87 41 98 FF                  call 0x140428374
00AA41ED  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA41F1  49 39 5C F8 08                  cmp qword ptr [r8 + rdi*8 + 8], rbx
00AA41F6  0F 84 40 02 00 00               je 0x140aa443c
00AA41FC  0F AE E8                        lfence
00AA41FF  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA4203  49 8B 44 F8 08                  mov rax, qword ptr [r8 + rdi*8 + 8]
00AA4208  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00AA420F  48 39 59 28                     cmp qword ptr [rcx + 0x28], rbx
00AA4213  0F 84 23 02 00 00               je 0x140aa443c
00AA4219  48 85 C0                        test rax, rax
00AA421C  74 19                           je 0x140aa4237
00AA421E  0F AE E8                        lfence
00AA4221  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA4225  49 8B 44 F8 08                  mov rax, qword ptr [r8 + rdi*8 + 8]
00AA422A  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00AA4231  48 8B 71 28                     mov rsi, qword ptr [rcx + 0x28]
00AA4235  EB 03                           jmp 0x140aa423a
00AA4237  48 8B F3                        mov rsi, rbx
00AA423A  49 39 5C F8 08                  cmp qword ptr [r8 + rdi*8 + 8], rbx
00AA423F  74 19                           je 0x140aa425a
00AA4241  0F AE E8                        lfence
00AA4244  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA4248  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA424D  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00AA4254  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00AA4258  EB 03                           jmp 0x140aa425d
00AA425A  48 8B CB                        mov rcx, rbx
00AA425D  BA 88 03 00 00                  mov edx, 0x388
00AA4262  E8 0D 41 98 FF                  call 0x140428374
00AA4267  66 39 5E 28                     cmp word ptr [rsi + 0x28], bx
00AA426B  74 1B                           je 0x140aa4288
00AA426D  BA 02 00 00 00                  mov edx, 2
00AA4272  48 8D 4E 28                     lea rcx, [rsi + 0x28]
00AA4276  E8 F9 40 98 FF                  call 0x140428374
00AA427B  0F B7 56 28                     movzx edx, word ptr [rsi + 0x28]
00AA427F  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AA4283  E8 EC 40 98 FF                  call 0x140428374
00AA4288  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA428C  49 39 5C F8 08                  cmp qword ptr [r8 + rdi*8 + 8], rbx
00AA4291  74 19                           je 0x140aa42ac
00AA4293  0F AE E8                        lfence
00AA4296  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA429A  49 8B 44 F8 08                  mov rax, qword ptr [r8 + rdi*8 + 8]
00AA429F  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00AA42A6  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00AA42AA  EB 03                           jmp 0x140aa42af
00AA42AC  48 8B C3                        mov rax, rbx
00AA42AF  66 39 58 38                     cmp word ptr [rax + 0x38], bx
00AA42B3  0F 84 8D 00 00 00               je 0x140aa4346
00AA42B9  49 39 5C F8 08                  cmp qword ptr [r8 + rdi*8 + 8], rbx
00AA42BE  74 19                           je 0x140aa42d9
00AA42C0  0F AE E8                        lfence
00AA42C3  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA42C7  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA42CC  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00AA42D3  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00AA42D7  EB 03                           jmp 0x140aa42dc
00AA42D9  48 8B CB                        mov rcx, rbx
00AA42DC  48 83 C1 38                     add rcx, 0x38
00AA42E0  BA 02 00 00 00                  mov edx, 2
00AA42E5  E8 8A 40 98 FF                  call 0x140428374
00AA42EA  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
00AA42EE  48 39 5C FA 08                  cmp qword ptr [rdx + rdi*8 + 8], rbx
00AA42F3  74 19                           je 0x140aa430e
00AA42F5  0F AE E8                        lfence
00AA42F8  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
00AA42FC  48 8B 44 FA 08                  mov rax, qword ptr [rdx + rdi*8 + 8]
00AA4301  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00AA4308  4C 8B 41 28                     mov r8, qword ptr [rcx + 0x28]
00AA430C  EB 03                           jmp 0x140aa4311
00AA430E  4C 8B C3                        mov r8, rbx
00AA4311  48 39 5C FA 08                  cmp qword ptr [rdx + rdi*8 + 8], rbx
00AA4316  74 19                           je 0x140aa4331
00AA4318  0F AE E8                        lfence
00AA431B  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA431F  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA4324  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00AA432B  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00AA432F  EB 03                           jmp 0x140aa4334
00AA4331  48 8B CB                        mov rcx, rbx
00AA4334  41 0F B7 50 38                  movzx edx, word ptr [r8 + 0x38]
00AA4339  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00AA433D  E8 32 40 98 FF                  call 0x140428374
00AA4342  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA4346  49 39 5C F8 08                  cmp qword ptr [r8 + rdi*8 + 8], rbx
00AA434B  74 19                           je 0x140aa4366
00AA434D  0F AE E8                        lfence
00AA4350  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA4354  49 8B 44 F8 08                  mov rax, qword ptr [r8 + rdi*8 + 8]
00AA4359  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00AA4360  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00AA4364  EB 03                           jmp 0x140aa4369
00AA4366  48 8B C3                        mov rax, rbx
00AA4369  48 39 58 10                     cmp qword ptr [rax + 0x10], rbx
00AA436D  0F 84 C9 00 00 00               je 0x140aa443c
00AA4373  49 39 5C F8 08                  cmp qword ptr [r8 + rdi*8 + 8], rbx
00AA4378  74 19                           je 0x140aa4393
00AA437A  0F AE E8                        lfence
00AA437D  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA4381  49 8B 44 F8 08                  mov rax, qword ptr [r8 + rdi*8 + 8]
00AA4386  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00AA438D  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00AA4391  EB 03                           jmp 0x140aa4396
00AA4393  48 8B C3                        mov rax, rbx
00AA4396  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00AA439A  66 39 58 38                     cmp word ptr [rax + 0x38], bx
00AA439E  0F 84 98 00 00 00               je 0x140aa443c
00AA43A4  49 39 5C F8 08                  cmp qword ptr [r8 + rdi*8 + 8], rbx
00AA43A9  74 19                           je 0x140aa43c4
00AA43AB  0F AE E8                        lfence
00AA43AE  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA43B2  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA43B7  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00AA43BE  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00AA43C2  EB 03                           jmp 0x140aa43c7
00AA43C4  48 8B CB                        mov rcx, rbx
00AA43C7  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00AA43CB  BA 02 00 00 00                  mov edx, 2
00AA43D0  48 83 C1 38                     add rcx, 0x38
00AA43D4  E8 9B 3F 98 FF                  call 0x140428374
00AA43D9  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
00AA43DD  48 39 5C FA 08                  cmp qword ptr [rdx + rdi*8 + 8], rbx
00AA43E2  74 19                           je 0x140aa43fd
00AA43E4  0F AE E8                        lfence
00AA43E7  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
00AA43EB  48 8B 44 FA 08                  mov rax, qword ptr [rdx + rdi*8 + 8]
00AA43F0  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00AA43F7  4C 8B 41 28                     mov r8, qword ptr [rcx + 0x28]
00AA43FB  EB 03                           jmp 0x140aa4400
00AA43FD  4C 8B C3                        mov r8, rbx
00AA4400  48 39 5C FA 08                  cmp qword ptr [rdx + rdi*8 + 8], rbx
00AA4405  74 19                           je 0x140aa4420
00AA4407  0F AE E8                        lfence
00AA440A  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA440E  48 8B 4C F8 08                  mov rcx, qword ptr [rax + rdi*8 + 8]
00AA4413  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00AA441A  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00AA441E  EB 03                           jmp 0x140aa4423
00AA4420  48 8B CB                        mov rcx, rbx
00AA4423  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
00AA4427  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00AA442B  0F B7 50 38                     movzx edx, word ptr [rax + 0x38]
00AA442F  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00AA4433  E8 3C 3F 98 FF                  call 0x140428374
00AA4438  4C 8B 45 30                     mov r8, qword ptr [rbp + 0x30]
00AA443C  4D 8B 44 F8 08                  mov r8, qword ptr [r8 + rdi*8 + 8]
00AA4441  45 33 C9                        xor r9d, r9d
00AA4444  B9 CA 00 00 00                  mov ecx, 0xca
00AA4449  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AA444E  41 8D 51 02                     lea edx, [r9 + 2]
00AA4452  E8 09 92 A5 FF                  call 0x1404fd660
00AA4457  CC                              int3
00AA4458  8B F3                           mov esi, ebx
00AA445A  49 8B CE                        mov rcx, r14
00AA445D  E8 C2 00 00 00                  call 0x140aa4524
00AA4462  85 F6                           test esi, esi
00AA4464  78 05                           js 0x140aa446b
00AA4466  85 C0                           test eax, eax
00AA4468  0F 48 F0                        cmovs esi, eax
00AA446B  49 8B CE                        mov rcx, r14
00AA446E  E8 F5 02 00 00                  call 0x140aa4768
00AA4473  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA4477  48 85 C0                        test rax, rax
00AA447A  74 24                           je 0x140aa44a0
00AA447C  39 18                           cmp dword ptr [rax], ebx
00AA447E  76 16                           jbe 0x140aa4496
00AA4480  8B CB                           mov ecx, ebx
00AA4482  48 8B 4C C8 08                  mov rcx, qword ptr [rax + rcx*8 + 8]
00AA4487  E8 C4 4E 85 FF                  call 0x1402f9350
00AA448C  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00AA4490  FF C3                           inc ebx
00AA4492  3B 18                           cmp ebx, dword ptr [rax]
00AA4494  72 EA                           jb 0x140aa4480
00AA4496  33 D2                           xor edx, edx
00AA4498  48 8B C8                        mov rcx, rax
00AA449B  E8 D0 E3 0D 00                  call 0x140b82870
00AA44A0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AA44A9  48 8D 0D B0 80 4E 00            lea rcx, [rip + 0x4e80b0]
00AA44B0  B2 01                           mov dl, 1
00AA44B2  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AA44B9  90                              nop
00AA44BA  E8 01 D7 76 FF                  call 0x140211bc0
00AA44BF  41 8B 96 2C 01 00 00            mov edx, dword ptr [r14 + 0x12c]
00AA44C6  8D 82 00 FD FF FF               lea eax, [rdx - 0x300]
00AA44CC  83 F8 02                        cmp eax, 2
00AA44CF  76 19                           jbe 0x140aa44ea
00AA44D1  8D 82 EB FC FF FF               lea eax, [rdx - 0x315]
00AA44D7  83 F8 01                        cmp eax, 1
00AA44DA  76 0E                           jbe 0x140aa44ea
00AA44DC  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00AA44E0  BA 13 00 00 00                  mov edx, 0x13
00AA44E5  E8 92 FF 00 00                  call 0x140ab447c
00AA44EA  48 8D 0D 6F 80 4E 00            lea rcx, [rip + 0x4e806f]
00AA44F1  E8 1A B5 7B FF                  call 0x14025fa10
00AA44F6  E8 B5 93 7B FF                  call 0x14025d8b0
00AA44FB  8B C6                           mov eax, esi
00AA44FD  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00AA4502  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00AA4507  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00AA450C  48 83 C4 30                     add rsp, 0x30
00AA4510  41 5F                           pop r15
00AA4512  41 5E                           pop r14
00AA4514  41 5D                           pop r13
00AA4516  41 5C                           pop r12
00AA4518  5D                              pop rbp
00AA4519  C3                              ret
00AA451A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiQueryPowerRelations(__int64 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (48);
    v_rbx = 0;
    v_stack_p8 = 0;
    if ((*(unsigned __int64 *)(a1 + 16)) != 0) goto loc_00AA3FD6;
    goto loc_00AA44FD;
loc_00AA3FD6:
    if (a2 != 0) goto loc_00AA445A;
    a3 = 0;
    result = PnpQueryDeviceRelations(*(unsigned __int64 *)(a1 + 32), a3 + 2, a3, v_stack_p8);
    if (!sign_flag) goto loc_00AA4001;
    v_stack_p8 = 0;
    goto loc_00AA445A;
loc_00AA4001:
    result = PnpAcquirePowerRelationsQueueLock(*(unsigned __int64 *)(a1 + 32), a3 + 2, a3, v_stack_p8);
    goto loc_00AA4069;
loc_00AA4013:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192)) + 8)) != (*(unsigned __int64 *)(a1 + 192))) goto loc_00AA4154;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 8))) != (*(unsigned __int64 *)(a1 + 192))) goto loc_00AA4154;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 24) + 8)) != (*(unsigned __int64 *)(a1 + 192) + 24)) goto loc_00AA4154;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 24 + 8))) != (*(unsigned __int64 *)(a1 + 192) + 24)) goto loc_00AA4154;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 24 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 24) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 24 + 8);
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 192), (unsigned int)(0x72775044ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 24), v_stack_p8);
loc_00AA4069:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192))) != (a1 + 192)) goto loc_00AA4013;
    result = PnpReleasePowerRelationsQueueLock(*(unsigned __int64 *)(a1 + 192), (unsigned int)(0x72775044ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192) + 24), v_stack_p8);
    if (v_stack_p8 == 0) goto loc_00AA4458;
    if ((*(unsigned int *)(v_stack_p8)) == 0) goto loc_00AA4458;
loc_00AA408C:
    if (0 >= (*(unsigned int *)(v_stack_p8))) goto loc_00AA445A;
    if (*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8) == 0) goto loc_00AA443C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8) + 312) + 40) == 0) goto loc_00AA4165;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8) + 312) + 40) + 396)) & (0x20000ULL)) != 0) goto loc_00AA4165;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8) + 312) + 40) + 16)) == 0) goto loc_00AA414C;
    result = ExAllocatePool2(56 + 8, 56, (unsigned int)(0x72775044ULL), v_stack_p8);
    if (result == 0) goto loc_00AA415B;
    *(unsigned __int8 *)(result + 48) = 0;
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8) + 312) + 40) + 160;
    *(unsigned __int64 *)(result + 16) = a1 + 160;
    result = PnpAcquirePowerRelationsQueueLock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8) + 312) + 40) + 160, 56, (unsigned int)(0x72775044ULL), v_stack_p8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192 + 8))) != (a1 + 192)) goto loc_00AA4154;
    *(unsigned __int64 *)(result) = a1 + 192;
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8) + 312) + 40)) + (176);
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 192 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 192 + 8)) = result;
    *(unsigned __int64 *)(a1 + 192 + 8) = result;
    v_rdi = (result) + (24);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8))) != v_r15) goto loc_00AA4154;
    *(unsigned __int64 *)(v_rdi) = v_r15;
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(v_r15 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8)) = v_rdi;
    *(unsigned __int64 *)(v_r15 + 8) = v_rdi;
    result = PnpReleasePowerRelationsQueueLock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8) + 312) + 40) + 160, 56, (unsigned int)(0x72775044ULL), v_stack_p8);
loc_00AA414C:
    v_r12 = (unsigned int)((0) + 1);
    goto loc_00AA408C;
loc_00AA4154:
loc_00AA415B:
    goto loc_00AA445A;
loc_00AA4165:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8) + 2), v_stack_p8, v_stack_p8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8) + 8)) == 0) goto loc_00AA41F1;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8) + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8) + 8) + 2)), v_stack_p8, v_stack_p8);
    result = *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8) + 8) + 56)) != 0) {
        result = v_stack_p8;
        a2 = 2;
        a1 = *(unsigned __int64 *)(result + v_rdi * 8 + 8);
        a1 = *(unsigned __int64 *)(a1 + 8);
        a1 = (a1) + (56);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p8, v_stack_p8);
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(result + v_rdi * 8 + 8);
        a1 = *(unsigned __int64 *)(a1 + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p8, v_stack_p8);
        a3 = v_stack_p8;
    }
    if ((*(unsigned __int64 *)(a3 + v_rdi * 8 + 8)) == 0) goto loc_00AA443C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8) + 312) + 40)) == 0) goto loc_00AA443C;
    if (*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8) == 0) goto loc_00AA4237;
    goto loc_00AA423A;
loc_00AA4237:
loc_00AA423A:
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA425A;
    goto loc_00AA425D;
loc_00AA425A:
loc_00AA425D:
    result = IoAddTriageDumpDataBlock(0, 904, v_stack_p8, v_stack_p8);
    if ((*(unsigned __int16 *)(0 + 40)) != 0) {
        a2 = 2;
        a1 = 0 + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p8, v_stack_p8);
        a2 = *(unsigned __int16 *)(0 + 40);
        a1 = *(unsigned __int64 *)(0 + 48);
        result = IoAddTriageDumpDataBlock(a1, a2, v_stack_p8, v_stack_p8);
    }
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA42AC;
    goto loc_00AA42AF;
loc_00AA42AC:
loc_00AA42AF:
    if ((*(unsigned __int16 *)(0 + 56)) == 0) goto loc_00AA4346;
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA42D9;
    goto loc_00AA42DC;
loc_00AA42D9:
loc_00AA42DC:
    a1 = (0) + (56);
    result = IoAddTriageDumpDataBlock(a1, 2, v_stack_p8, v_stack_p8);
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA430E;
    goto loc_00AA4311;
loc_00AA430E:
loc_00AA4311:
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA4331;
    goto loc_00AA4334;
loc_00AA4331:
loc_00AA4334:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(0 + 64), *(unsigned __int16 *)(0 + 56), 0, v_stack_p8);
loc_00AA4346:
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA4366;
    goto loc_00AA4369;
loc_00AA4366:
loc_00AA4369:
    if ((*(unsigned __int64 *)(0 + 16)) == 0) goto loc_00AA443C;
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA4393;
    goto loc_00AA4396;
loc_00AA4393:
loc_00AA4396:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(0 + 16) + 56)) == 0) goto loc_00AA443C;
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA43C4;
    goto loc_00AA43C7;
loc_00AA43C4:
loc_00AA43C7:
    a1 = (*(unsigned __int64 *)(0 + 16)) + (56);
    result = IoAddTriageDumpDataBlock(a1, 2, v_stack_p8, v_stack_p8);
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA43FD;
    goto loc_00AA4400;
loc_00AA43FD:
loc_00AA4400:
    if ((*(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8)) == 0) goto loc_00AA4420;
    goto loc_00AA4423;
loc_00AA4420:
loc_00AA4423:
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 16) + 64), *(unsigned __int16 *)(*(unsigned __int64 *)(0 + 16) + 56), 0, v_stack_p8);
loc_00AA443C:
    a4 = 0;
    v_stack_m38 = 0;
    result = KeBugCheckEx(202, a4 + 2, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
loc_00AA4458:
loc_00AA445A:
    result = PiQueryPowerDependencyRelations(a1, a4 + 2, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
    v_rsi = 0;
    if (!(sign_flag)) {
        v_rsi = 0;
        if (sign_flag) { v_rsi = (unsigned int)(result); }
    }
    result = PiValidatePowerRelations(a1, a4 + 2, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
    if (v_stack_p8 == 0) goto loc_00AA44A0;
    if ((*(unsigned int *)(v_stack_p8)) <= 0) goto loc_00AA4496;
loc_00AA4480:
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 8), a4 + 2, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((unsigned int)(v_rbx)) < (*(unsigned int *)(v_stack_p8))) goto loc_00AA4480;
loc_00AA4496:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p8, a2, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
loc_00AA44A0:
    result = ExAcquireResourceSharedLite(v_rip + 5144752, 1, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)) - 768)) <= 2) goto loc_00AA44EA;
    result = (unsigned int)(*(unsigned int *)(a1 + 300)) - 789;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)) - 789)) >= = 1) {
        a1 = *(unsigned __int64 *)(a1 + 32);
        a2 = 19;
        result = PiPnpRtlPdoRaiseNtPlugPlayPropertyChangeEvent(a1, a2, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
    }
    result = ExReleaseResourceLite(v_rip + 5144687, a2, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
    result = KeLeaveCriticalRegion(v_rip + 5144687, a2, *(unsigned __int64 *)(v_stack_p8 + v_rdi * 8 + 8), a4);
loc_00AA44FD:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)(v_rsi));
}
```

## 5. (Beta) C Style

```c
int64_t PiQueryPowerRelations(void *Arg1, uint8_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (48);
    local_rbx = 0;
    v_stack_p8 = 0;
    if ((*(uint64_t *)(arg1 + 0x10)) != 0) goto loc_00AA3FD6;
    goto loc_00AA44FD;
loc_00AA3FD6:
    if (Arg2 != 0) goto loc_00AA445A;
    Arg3 = 0;
    result = PnpQueryDeviceRelations(*(uint64_t *)(arg1 + 0x20), Arg3 + 2, Arg3, v_stack_p8);
    if (!sign_flag) goto loc_00AA4001;
    v_stack_p8 = 0;
    goto loc_00AA445A;
loc_00AA4001:
    result = PnpAcquirePowerRelationsQueueLock(*(uint64_t *)(arg1 + 0x20), Arg3 + 2, Arg3, v_stack_p8);
    goto loc_00AA4069;
loc_00AA4013:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0)) + 0x8)) != (*(uint64_t *)(arg1 + 0xC0))) goto loc_00AA4154;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x8))) != (*(uint64_t *)(arg1 + 0xC0))) goto loc_00AA4154;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xC0));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0)) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x18) + 0x8)) != (*(uint64_t *)(arg1 + 0xC0) + 24)) goto loc_00AA4154;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x18 + 0x8))) != (*(uint64_t *)(arg1 + 0xC0) + 24)) goto loc_00AA4154;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x18 + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x18);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x18) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x18 + 0x8);
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0xC0), (uint32_t)(0x72775044ULL), *(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x18), v_stack_p8);
loc_00AA4069:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0))) != (Arg1 + 192)) goto loc_00AA4013;
    result = PnpReleasePowerRelationsQueueLock(*(uint64_t *)(arg1 + 0xC0), (uint32_t)(0x72775044ULL), *(uint64_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x18), v_stack_p8);
    if (v_stack_p8 == 0) goto loc_00AA4458;
    if ((*(uint32_t *)(v_stack_p8)) == 0) goto loc_00AA4458;
loc_00AA408C:
    if (0 >= (*(uint32_t *)(v_stack_p8))) goto loc_00AA445A;
    if (*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8) == 0) goto loc_00AA443C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8) + 0x138) + 0x28) == 0) goto loc_00AA4165;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8) + 0x138) + 0x28) + 0x18C)) & (0x20000ULL)) != 0) goto loc_00AA4165;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8) + 0x138) + 0x28) + 0x10)) == 0) goto loc_00AA414C;
    result = ExAllocatePool2(56 + 8, 56, (uint32_t)(0x72775044ULL), v_stack_p8);
    if (result == 0) goto loc_00AA415B;
    *(uint8_t *)(result + 0x30) = 0;
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8) + 0x138) + 0x28) + 160;
    *(void **)(result + 0x10) = Arg1 + 160;
    result = PnpAcquirePowerRelationsQueueLock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8) + 0x138) + 0x28) + 160, 56, (uint32_t)(0x72775044ULL), v_stack_p8);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xC0 + 0x8))) != (Arg1 + 192)) goto loc_00AA4154;
    *(void **)(result) = Arg1 + 192;
    local_r15 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8) + 0x138) + 0x28)) + (176);
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1 + 0xC0 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0xC0 + 0x8)) = result;
    *(uint64_t *)(arg1 + 0xC0 + 0x8) = result;
    local_rdi = (result) + (24);
    if ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8))) != local_r15) goto loc_00AA4154;
    *(uint64_t *)(local_rdi) = local_r15;
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(local_r15 + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8)) = local_rdi;
    *(uint64_t *)(local_r15 + 0x8) = local_rdi;
    result = PnpReleasePowerRelationsQueueLock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8) + 0x138) + 0x28) + 160, 56, (uint32_t)(0x72775044ULL), v_stack_p8);
loc_00AA414C:
    local_r12 = (uint32_t)((0) + 1);
    goto loc_00AA408C;
loc_00AA4154:
loc_00AA415B:
    goto loc_00AA445A;
loc_00AA4165:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), *(uint16_t *)(*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8) + 0x2), v_stack_p8, v_stack_p8);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8) + 0x8)) == 0) goto loc_00AA41F1;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8) + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8) + 0x8) + 0x2)), v_stack_p8, v_stack_p8);
    result = *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8) + 0x8) + 0x38)) != 0) {
        result = v_stack_p8;
        Arg2 = 2;
        Arg1 = *(uint64_t *)(result + local_rdi * 8 + 0x8);
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        Arg1 = (Arg1) + (56);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p8, v_stack_p8);
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(result + local_rdi * 8 + 0x8);
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p8, v_stack_p8);
        Arg3 = v_stack_p8;
    }
    if ((*(uint64_t *)(Arg3 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA443C;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8) + 0x138) + 0x28)) == 0) goto loc_00AA443C;
    if (*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8) == 0) goto loc_00AA4237;
    goto loc_00AA423A;
loc_00AA4237:
loc_00AA423A:
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA425A;
    goto loc_00AA425D;
loc_00AA425A:
loc_00AA425D:
    result = IoAddTriageDumpDataBlock(0, 904, v_stack_p8, v_stack_p8);
    if ((*(uint16_t *)(0 + 0x28)) != 0) {
        Arg2 = 2;
        Arg1 = 0 + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p8, v_stack_p8);
        Arg2 = *(uint16_t *)(0 + 0x28);
        Arg1 = *(uint64_t *)(0 + 0x30);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, v_stack_p8, v_stack_p8);
    }
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA42AC;
    goto loc_00AA42AF;
loc_00AA42AC:
loc_00AA42AF:
    if ((*(uint16_t *)(0 + 0x38)) == 0) goto loc_00AA4346;
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA42D9;
    goto loc_00AA42DC;
loc_00AA42D9:
loc_00AA42DC:
    Arg1 = (0) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, 2, v_stack_p8, v_stack_p8);
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA430E;
    goto loc_00AA4311;
loc_00AA430E:
loc_00AA4311:
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA4331;
    goto loc_00AA4334;
loc_00AA4331:
loc_00AA4334:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(0 + 0x40), *(uint16_t *)(0 + 0x38), 0, v_stack_p8);
loc_00AA4346:
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA4366;
    goto loc_00AA4369;
loc_00AA4366:
loc_00AA4369:
    if ((*(uint64_t *)(0 + 0x10)) == 0) goto loc_00AA443C;
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA4393;
    goto loc_00AA4396;
loc_00AA4393:
loc_00AA4396:
    if ((*(uint16_t *)(*(uint64_t *)(0 + 0x10) + 0x38)) == 0) goto loc_00AA443C;
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA43C4;
    goto loc_00AA43C7;
loc_00AA43C4:
loc_00AA43C7:
    Arg1 = (*(uint64_t *)(0 + 0x10)) + (56);
    result = IoAddTriageDumpDataBlock(Arg1, 2, v_stack_p8, v_stack_p8);
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA43FD;
    goto loc_00AA4400;
loc_00AA43FD:
loc_00AA4400:
    if ((*(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8)) == 0) goto loc_00AA4420;
    goto loc_00AA4423;
loc_00AA4420:
loc_00AA4423:
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(0 + 0x10) + 0x40), *(uint16_t *)(*(uint64_t *)(0 + 0x10) + 0x38), 0, v_stack_p8);
loc_00AA443C:
    a4 = 0;
    v_stack_m38 = 0;
    result = KeBugCheckEx(202, a4 + 2, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
loc_00AA4458:
loc_00AA445A:
    result = PiQueryPowerDependencyRelations(Arg1, a4 + 2, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
    local_rsi = 0;
    if (!(sign_flag)) {
        local_rsi = 0;
        if (sign_flag) { local_rsi = (uint32_t)(result); }
    }
    result = PiValidatePowerRelations(Arg1, a4 + 2, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
    if (v_stack_p8 == 0) goto loc_00AA44A0;
    if ((*(uint32_t *)(v_stack_p8)) <= 0) goto loc_00AA4496;
loc_00AA4480:
    result = ObfDereferenceObject(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x8), a4 + 2, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((uint32_t)(local_rbx)) < (*(uint32_t *)(v_stack_p8))) goto loc_00AA4480;
loc_00AA4496:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p8, Arg2, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
loc_00AA44A0:
    result = ExAcquireResourceSharedLite(v_rip + 5144752, 1, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)) - 768)) <= 2) goto loc_00AA44EA;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x12C)) - 789;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)) - 789)) >= = 1) {
        Arg1 = *(uint64_t *)(arg1 + 0x20);
        Arg2 = 19;
        result = PiPnpRtlPdoRaiseNtPlugPlayPropertyChangeEvent(Arg1, Arg2, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
    }
    result = ExReleaseResourceLite(v_rip + 5144687, Arg2, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
    result = KeLeaveCriticalRegion(v_rip + 5144687, Arg2, *(uint64_t *)(v_stack_p8 + local_rdi * 8 + 0x8), a4);
loc_00AA44FD:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)(local_rsi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0x12C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA3F9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
