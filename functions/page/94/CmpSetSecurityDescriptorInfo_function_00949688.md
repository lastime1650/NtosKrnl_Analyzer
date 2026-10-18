# CmpSetSecurityDescriptorInfo

- RVA: `0x00949688`–`0x00949DFC` (길이 `1,908` bytes)
- VA: `0x0000000140949688`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00090D28`
- 디코드: `482`개 명령, `1,908/1,908` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **53**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00949727` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00949742` → [CmpUpdateKeyNodeAccessBits](../84/CmpUpdateKeyNodeAccessBits_function_0084864C.md) (function, `0x0084864C`)
- `0x0094974E` → [CmGetKCBCacheSecurity](CmGetKCBCacheSecurity_function_00949E10.md) (function, `0x00949E10`)
- `0x0094976D` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0094978C` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x009497A9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009497E6` → [RtlpSetSecurityObject](../8B/RtlpSetSecurityObject_function_008BB500.md) (function, `0x008BB500`)
- `0x00949810` → [CmpTraceSecurityChanging](CmpTraceSecurityChanging_function_00949EEC.md) (function, `0x00949EEC`)
- `0x00949823` → [RtlLengthSecurityDescriptorStrict](../../text/48/RtlLengthSecurityDescriptorStrict_function_0048B770.md) (function, `0x0048B770`)
- `0x0094985E` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00949879` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x0094989F` → [CmpFindMatchingDescriptorCell](CmpFindMatchingDescriptorCell_function_009494A0.md) (function, `0x009494A0`)
- `0x009498CA` → [CmpKeySecurityIncrementReferenceCount](../../text/49/CmpKeySecurityIncrementReferenceCount_function_0049FC64.md) (function, `0x0049FC64`)
- `0x009498EA` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x009498F4` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00949902` → [RtlLengthSecurityDescriptorStrict](../../text/48/RtlLengthSecurityDescriptorStrict_function_0048B770.md) (function, `0x0048B770`)
- `0x00949926` → [HvAllocateCell](../85/HvAllocateCell_function_00859C94.md) (function, `0x00859C94`)
- `0x00949948` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00949959` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0094998B` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009499A9` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009499C2` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x009499EA` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00949A2D` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00949A4A` → [CmpKeySecurityIncrementReferenceCount](../../text/49/CmpKeySecurityIncrementReferenceCount_function_0049FC64.md) (function, `0x0049FC64`)
- `0x00949A69` → [CmpKeySecurityDecrementReferenceCount](../../text/4A/CmpKeySecurityDecrementReferenceCount_function_004A67DC.md) (function, `0x004A67DC`)
- `0x00949A85` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00949AF3` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (function, `0x00428060`)
- `0x00949B24` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00949B39` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00949B43` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00949B4D` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00949B71` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00949B89` → [CmpKeySecurityMarkDirtyForReferenceCountDecrement](../../text/4D/CmpKeySecurityMarkDirtyForReferenceCountDecrement_function_004D6608.md) (function, `0x004D6608`)
- `0x00949BB0` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00949BE7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00949BF5` → [CmpAddSecurityCellToCache](../96/CmpAddSecurityCellToCache_function_0096E228.md) (function, `0x0096E228`)
- `0x00949C21` → [CmpKeySecurityDecrementReferenceCount](../../text/4A/CmpKeySecurityDecrementReferenceCount_function_004A67DC.md) (function, `0x004A67DC`)
- `0x00949C39` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00949C50` → [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) (function, `0x004BC1FC`)
- `0x00949C5B` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x00949C65` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00949C6F` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00949C97` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00949CC7` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x00949D18` → [CmpKeySecurityMarkDirtyForReferenceCountDecrement](../../text/4D/CmpKeySecurityMarkDirtyForReferenceCountDecrement_function_004D6608.md) (function, `0x004D6608`)
- `0x00949D4B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00949D57` → [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) (function, `0x004BC1FC`)
- `0x00949D62` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x00949D9B` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (function, `0x00428060`)
- `0x00949DBD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00949DD4` → [HvFreeCell](../85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)
- `0x00949DF2` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- [CmpSetKeySecurity](CmpSetKeySecurity_function_0094A124.md) at `0x0094A36D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **20**
  - `0x0094978C` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x009497A9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00949823` → [RtlLengthSecurityDescriptorStrict](../../text/48/RtlLengthSecurityDescriptorStrict_function_0048B770.md) (`PAGE` → `.text`)
  - `0x009498CA` → [CmpKeySecurityIncrementReferenceCount](../../text/49/CmpKeySecurityIncrementReferenceCount_function_0049FC64.md) (`PAGE` → `.text`)
  - `0x00949902` → [RtlLengthSecurityDescriptorStrict](../../text/48/RtlLengthSecurityDescriptorStrict_function_0048B770.md) (`PAGE` → `.text`)
  - `0x00949948` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00949959` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00949A4A` → [CmpKeySecurityIncrementReferenceCount](../../text/49/CmpKeySecurityIncrementReferenceCount_function_0049FC64.md) (`PAGE` → `.text`)
  - `0x00949A69` → [CmpKeySecurityDecrementReferenceCount](../../text/4A/CmpKeySecurityDecrementReferenceCount_function_004A67DC.md) (`PAGE` → `.text`)
  - `0x00949AF3` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (`PAGE` → `.text`)
  - `0x00949B89` → [CmpKeySecurityMarkDirtyForReferenceCountDecrement](../../text/4D/CmpKeySecurityMarkDirtyForReferenceCountDecrement_function_004D6608.md) (`PAGE` → `.text`)
  - `0x00949BE7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00949C21` → [CmpKeySecurityDecrementReferenceCount](../../text/4A/CmpKeySecurityDecrementReferenceCount_function_004A67DC.md) (`PAGE` → `.text`)
  - `0x00949C50` → [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) (`PAGE` → `.text`)
  - `0x00949C97` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00949D18` → [CmpKeySecurityMarkDirtyForReferenceCountDecrement](../../text/4D/CmpKeySecurityMarkDirtyForReferenceCountDecrement_function_004D6608.md) (`PAGE` → `.text`)
  - `0x00949D4B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00949D57` → [CmpRemoveSecurityCellList](../../text/4B/CmpRemoveSecurityCellList_function_004BC1FC.md) (`PAGE` → `.text`)
  - `0x00949D9B` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (`PAGE` → `.text`)
  - `0x00949DBD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00949BAA` → [sub_00B25C42 + 0xA](../B2/Unknown_function_00B25C42.md) (`tail-transfer`)
  - `0x00949BB6` → [sub_00B25C42 + 0xF](../B2/Unknown_function_00B25C42.md) (`tail-transfer`)
  - `0x00949D31` → [sub_00B25C42](../B2/Unknown_function_00B25C42.md) (`tail-transfer`)
  - `0x00949DA2` → [sub_00B25C42 + 0x38](../B2/Unknown_function_00B25C42.md) (`tail-transfer`)
  - `0x00949DCA` → [sub_00B25C42 + 0x5A](../B2/Unknown_function_00B25C42.md) (`tail-transfer`)
  - `0x00949DEC` → [sub_00B25C42 + 0xCD](../B2/Unknown_function_00B25C42.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00949688  48 8B C4                        mov rax, rsp
0094968B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0094968F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00949693  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00949697  48 89 48 08                     mov qword ptr [rax + 8], rcx
0094969B  55                              push rbp
0094969C  53                              push rbx
0094969D  56                              push rsi
0094969E  57                              push rdi
0094969F  41 54                           push r12
009496A1  41 55                           push r13
009496A3  41 56                           push r14
009496A5  41 57                           push r15
009496A7  48 8D 68 B9                     lea rbp, [rax - 0x47]
009496AB  48 81 EC B8 00 00 00            sub rsp, 0xb8
009496B2  45 33 E4                        xor r12d, r12d
009496B5  48 8B D9                        mov rbx, rcx
009496B8  83 C9 FF                        or ecx, 0xffffffff
009496BB  4C 89 65 9F                     mov qword ptr [rbp - 0x61], r12
009496BF  0F 57 C0                        xorps xmm0, xmm0
009496C2  89 4D 97                        mov dword ptr [rbp - 0x69], ecx
009496C5  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
009496C9  48 8B 7B 20                     mov rdi, qword ptr [rbx + 0x20]
009496CD  49 8B F0                        mov rsi, r8
009496D0  44 8B 7B 28                     mov r15d, dword ptr [rbx + 0x28]
009496D4  4C 8D 45 BF                     lea r8, [rbp - 0x41]
009496D8  89 4D A7                        mov dword ptr [rbp - 0x59], ecx
009496DB  45 8B F4                        mov r14d, r12d
009496DE  89 4D B7                        mov dword ptr [rbp - 0x49], ecx
009496E1  41 8B D7                        mov edx, r15d
009496E4  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
009496EB  89 4D BF                        mov dword ptr [rbp - 0x41], ecx
009496EE  48 8B CF                        mov rcx, rdi
009496F1  44 89 65 C7                     mov dword ptr [rbp - 0x39], r12d
009496F5  44 89 65 CB                     mov dword ptr [rbp - 0x35], r12d
009496F9  44 89 65 67                     mov dword ptr [rbp + 0x67], r12d
009496FD  44 89 65 9B                     mov dword ptr [rbp - 0x65], r12d
00949701  44 89 65 AB                     mov dword ptr [rbp - 0x55], r12d
00949705  44 89 65 BB                     mov dword ptr [rbp - 0x45], r12d
00949709  44 89 65 C3                     mov dword ptr [rbp - 0x3d], r12d
0094970D  4C 89 65 E7                     mov qword ptr [rbp - 0x19], r12
00949711  4C 89 65 8F                     mov qword ptr [rbp - 0x71], r12
00949715  4C 89 65 AF                     mov qword ptr [rbp - 0x51], r12
00949719  4C 89 65 D7                     mov qword ptr [rbp - 0x29], r12
0094971D  44 89 7D DF                     mov dword ptr [rbp - 0x21], r15d
00949721  0F 84 C3 01 00 00               je 0x1409498ea
00949727  E8 34 B5 F0 FF                  call 0x140854c60
0094972C  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00949730  48 85 C0                        test rax, rax
00949733  0F 84 64 05 00 00               je 0x140949c9d
00949739  45 8B C7                        mov r8d, r15d
0094973C  48 8B D0                        mov rdx, rax
0094973F  48 8B CF                        mov rcx, rdi
00949742  E8 05 EF EF FF                  call 0x14084864c
00949747  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
0094974B  48 8B CB                        mov rcx, rbx
0094974E  E8 BD 06 00 00                  call 0x140949e10
00949753  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
0094975A  4C 8D 45 97                     lea r8, [rbp - 0x69]
0094975E  48 8B CF                        mov rcx, rdi
00949761  44 8B 20                        mov r12d, dword ptr [rax]
00949764  41 8B D4                        mov edx, r12d
00949767  0F 84 87 01 00 00               je 0x1409498f4
0094976D  E8 EE B4 F0 FF                  call 0x140854c60
00949772  4C 8B E8                        mov r13, rax
00949775  48 85 C0                        test rax, rax
00949778  0F 84 29 05 00 00               je 0x140949ca7
0094977E  8B 50 10                        mov edx, dword ptr [rax + 0x10]
00949781  B9 00 01 00 00                  mov ecx, 0x100
00949786  41 B8 43 4D 38 36               mov r8d, 0x36384d43
0094978C  E8 73 3D A8 FF                  call 0x1403cd504
00949791  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00949795  48 85 C0                        test rax, rax
00949798  0F 84 09 05 00 00               je 0x140949ca7
0094979E  45 8B 45 10                     mov r8d, dword ptr [r13 + 0x10]
009497A2  49 8D 55 14                     lea rdx, [r13 + 0x14]
009497A6  48 8B C8                        mov rcx, rax
009497A9  E8 92 D0 D7 FF                  call 0x1406c6840
009497AE  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
009497B2  4C 8D 4D 9F                     lea r9, [rbp - 0x61]
009497B6  48 8B 55 57                     mov rdx, qword ptr [rbp + 0x57]
009497BA  4C 8B C6                        mov r8, rsi
009497BD  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
009497C1  33 C9                           xor ecx, ecx
009497C3  48 8B 85 8F 00 00 00            mov rax, qword ptr [rbp + 0x8f]
009497CA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009497CF  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
009497D3  8B 12                           mov edx, dword ptr [rdx]
009497D5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009497DA  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
009497DD  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
009497E1  44 21 74 24 20                  and dword ptr [rsp + 0x20], r14d
009497E6  E8 15 1D F7 FF                  call 0x1408bb500
009497EB  8B F0                           mov esi, eax
009497ED  85 C0                           test eax, eax
009497EF  0F 88 BF 04 00 00               js 0x140949cb4
009497F5  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
009497F9  48 8B CB                        mov rcx, rbx
009497FC  4C 8B 4D 5F                     mov r9, qword ptr [rbp + 0x5f]
00949800  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
00949804  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00949809  48 8B 45 57                     mov rax, qword ptr [rbp + 0x57]
0094980D  44 8B 00                        mov r8d, dword ptr [rax]
00949810  E8 D7 06 00 00                  call 0x140949eec
00949815  8B F0                           mov esi, eax
00949817  85 C0                           test eax, eax
00949819  0F 88 8D 04 00 00               js 0x140949cac
0094981F  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00949823  E8 48 1F B4 FF                  call 0x14048b770
00949828  4C 8B 75 7F                     mov r14, qword ptr [rbp + 0x7f]
0094982C  89 45 5F                        mov dword ptr [rbp + 0x5f], eax
0094982F  4D 85 F6                        test r14, r14
00949832  0F 85 F6 02 00 00               jne 0x140949b2e
00949838  41 C1 EF 1F                     shr r15d, 0x1f
0094983C  48 BB 14 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000014
00949846  45 33 C9                        xor r9d, r9d
00949849  45 33 C0                        xor r8d, r8d
0094984C  48 8B CF                        mov rcx, rdi
0094984F  48 8B 1B                        mov rbx, qword ptr [rbx]
00949852  4D 85 F6                        test r14, r14
00949855  0F 85 69 04 00 00               jne 0x140949cc4
0094985B  8B 55 DF                        mov edx, dword ptr [rbp - 0x21]
0094985E  E8 1D E8 F0 FF                  call 0x140858080
00949863  8B F0                           mov esi, eax
00949865  85 C0                           test eax, eax
00949867  0F 88 C8 00 00 00               js 0x140949935
0094986D  45 33 C9                        xor r9d, r9d
00949870  45 33 C0                        xor r8d, r8d
00949873  41 8B D4                        mov edx, r12d
00949876  48 8B CF                        mov rcx, rdi
00949879  E8 02 E8 F0 FF                  call 0x140858080
0094987E  8B F0                           mov esi, eax
00949880  85 C0                           test eax, eax
00949882  0F 88 AD 00 00 00               js 0x140949935
00949888  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
0094988C  48 8D 45 E7                     lea rax, [rbp - 0x19]
00949890  4C 8D 4D C7                     lea r9, [rbp - 0x39]
00949894  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00949899  45 8B C7                        mov r8d, r15d
0094989C  48 8B CF                        mov rcx, rdi
0094989F  E8 FC FB FF FF                  call 0x1409494a0
009498A4  84 C0                           test al, al
009498A6  74 56                           je 0x1409498fe
009498A8  44 8B 7D C7                     mov r15d, dword ptr [rbp - 0x39]
009498AC  45 3B FC                        cmp r15d, r12d
009498AF  0F 85 29 01 00 00               jne 0x1409499de
009498B5  4D 85 F6                        test r14, r14
009498B8  0F 84 38 04 00 00               je 0x140949cf6
009498BE  45 33 C9                        xor r9d, r9d
009498C1  45 8B C7                        mov r8d, r15d
009498C4  48 8B D7                        mov rdx, rdi
009498C7  49 8B CD                        mov rcx, r13
009498CA  E8 95 63 B5 FF                  call 0x14049fc64
009498CF  8B F0                           mov esi, eax
009498D1  85 C0                           test eax, eax
009498D3  78 60                           js 0x140949935
009498D5  48 8B 95 87 00 00 00            mov rdx, qword ptr [rbp + 0x87]
009498DC  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
009498E0  44 89 7A 60                     mov dword ptr [rdx + 0x60], r15d
009498E4  48 89 42 58                     mov qword ptr [rdx + 0x58], rax
009498E8  EB 4B                           jmp 0x140949935
009498EA  E8 C1 B3 F0 FF                  call 0x140854cb0
009498EF  E9 38 FE FF FF                  jmp 0x14094972c
009498F4  E8 B7 B3 F0 FF                  call 0x140854cb0
009498F9  E9 74 FE FF FF                  jmp 0x140949772
009498FE  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00949902  E8 69 1E B4 FF                  call 0x14048b770
00949907  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0094990B  45 8B C7                        mov r8d, r15d
0094990E  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00949913  4C 8D 4D CB                     lea r9, [rbp - 0x35]
00949917  48 8D 4D AF                     lea rcx, [rbp - 0x51]
0094991B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00949920  8D 50 14                        lea edx, [rax + 0x14]
00949923  48 8B CF                        mov rcx, rdi
00949926  E8 69 03 F1 FF                  call 0x140859c94
0094992B  8B F0                           mov esi, eax
0094992D  85 C0                           test eax, eax
0094992F  0F 89 22 02 00 00               jns 0x140949b57
00949935  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00949939  48 8B 5D 8F                     mov rbx, qword ptr [rbp - 0x71]
0094993D  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00949941  48 85 C9                        test rcx, rcx
00949944  74 07                           je 0x14094994d
00949946  33 D2                           xor edx, edx
00949948  E8 23 8F 23 00                  call 0x140b82870
0094994D  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
00949951  48 85 C0                        test rax, rax
00949954  74 08                           je 0x14094995e
00949956  48 8B C8                        mov rcx, rax
00949959  E8 22 C4 B2 FF                  call 0x140475d80
0094995E  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
00949961  85 C0                           test eax, eax
00949963  0F 85 66 04 00 00               jne 0x140949dcf
00949969  48 85 DB                        test rbx, rbx
0094996C  0F 85 6C 04 00 00               jne 0x140949dde
00949972  4D 85 F6                        test r14, r14
00949975  74 19                           je 0x140949990
00949977  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
0094997E  48 8D 55 A7                     lea rdx, [rbp - 0x59]
00949982  48 8B CF                        mov rcx, rdi
00949985  0F 85 C2 01 00 00               jne 0x140949b4d
0094998B  E8 B0 C5 F0 FF                  call 0x140855f40
00949990  4D 85 ED                        test r13, r13
00949993  74 19                           je 0x1409499ae
00949995  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
0094999C  48 8D 55 97                     lea rdx, [rbp - 0x69]
009499A0  48 8B CF                        mov rcx, rdi
009499A3  0F 85 9A 01 00 00               jne 0x140949b43
009499A9  E8 92 C5 F0 FF                  call 0x140855f40
009499AE  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
009499B5  48 8D 55 BF                     lea rdx, [rbp - 0x41]
009499B9  48 8B CF                        mov rcx, rdi
009499BC  0F 85 77 01 00 00               jne 0x140949b39
009499C2  E8 79 C5 F0 FF                  call 0x140855f40
009499C7  8B C6                           mov eax, esi
009499C9  48 81 C4 B8 00 00 00            add rsp, 0xb8
009499D0  41 5F                           pop r15
009499D2  41 5E                           pop r14
009499D4  41 5D                           pop r13
009499D6  41 5C                           pop r12
009499D8  5F                              pop rdi
009499D9  5E                              pop rsi
009499DA  5B                              pop rbx
009499DB  5D                              pop rbp
009499DC  C3                              ret
009499DD  CC                              int3
009499DE  45 33 C9                        xor r9d, r9d
009499E1  45 33 C0                        xor r8d, r8d
009499E4  41 8B D7                        mov edx, r15d
009499E7  48 8B CF                        mov rcx, rdi
009499EA  E8 91 E6 F0 FF                  call 0x140858080
009499EF  8B F0                           mov esi, eax
009499F1  85 C0                           test eax, eax
009499F3  0F 88 3C FF FF FF               js 0x140949935
009499F9  4D 85 F6                        test r14, r14
009499FC  0F 84 0D 03 00 00               je 0x140949d0f
00949A02  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00949A06  48 8B 95 87 00 00 00            mov rdx, qword ptr [rbp + 0x87]
00949A0D  8B 01                           mov eax, dword ptr [rcx]
00949A0F  89 42 60                        mov dword ptr [rdx + 0x60], eax
00949A12  48 89 4A 58                     mov qword ptr [rdx + 0x58], rcx
00949A16  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00949A1D  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00949A21  41 8B D7                        mov edx, r15d
00949A24  48 8B CF                        mov rcx, rdi
00949A27  0F 84 F7 00 00 00               je 0x140949b24
00949A2D  E8 2E B2 F0 FF                  call 0x140854c60
00949A32  4C 8B F0                        mov r14, rax
00949A35  48 85 C0                        test rax, rax
00949A38  0F 84 EE 02 00 00               je 0x140949d2c
00949A3E  45 33 C9                        xor r9d, r9d
00949A41  45 8B C7                        mov r8d, r15d
00949A44  48 8B D7                        mov rdx, rdi
00949A47  48 8B C8                        mov rcx, rax
00949A4A  E8 15 62 B5 FF                  call 0x14049fc64
00949A4F  8B F0                           mov esi, eax
00949A51  85 C0                           test eax, eax
00949A53  0F 88 E0 FE FF FF               js 0x140949939
00949A59  48 83 7D 7F 00                  cmp qword ptr [rbp + 0x7f], 0
00949A5E  75 3F                           jne 0x140949a9f
00949A60  45 8B C4                        mov r8d, r12d
00949A63  48 8B D7                        mov rdx, rdi
00949A66  49 8B CD                        mov rcx, r13
00949A69  E8 6E CD B5 FF                  call 0x1404a67dc
00949A6E  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00949A75  48 8D 55 97                     lea rdx, [rbp - 0x69]
00949A79  88 45 5F                        mov byte ptr [rbp + 0x5f], al
00949A7C  48 8B CF                        mov rcx, rdi
00949A7F  0F 85 E0 01 00 00               jne 0x140949c65
00949A85  E8 B6 C4 F0 FF                  call 0x140855f40
00949A8A  45 33 ED                        xor r13d, r13d
00949A8D  44 38 6D 5F                     cmp byte ptr [rbp + 0x5f], r13b
00949A91  0F 85 BA 02 00 00               jne 0x140949d51
00949A97  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00949A9B  44 89 78 2C                     mov dword ptr [rax + 0x2c], r15d
00949A9F  48 83 65 8F 00                  and qword ptr [rbp - 0x71], 0
00949AA4  45 8B FC                        mov r15d, r12d
00949AA7  48 83 7D 7F 00                  cmp qword ptr [rbp + 0x7f], 0
00949AAC  0F 85 11 03 00 00               jne 0x140949dc3
00949AB2  4C 8B 65 4F                     mov r12, qword ptr [rbp + 0x4f]
00949AB6  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00949ABA  83 65 4F 00                     and dword ptr [rbp + 0x4f], 0
00949ABE  48 89 58 04                     mov qword ptr [rax + 4], rbx
00949AC2  49 FF 84 24 30 01 00 00         inc qword ptr [r12 + 0x130]
00949ACA  49 89 9C 24 A8 00 00 00         mov qword ptr [r12 + 0xa8], rbx
00949AD2  44 8B 78 2C                     mov r15d, dword ptr [rax + 0x2c]
00949AD6  41 83 FF FF                     cmp r15d, -1
00949ADA  0F 84 96 01 00 00               je 0x140949c76
00949AE0  49 8B 44 24 20                  mov rax, qword ptr [r12 + 0x20]
00949AE5  4C 8D 45 4F                     lea r8, [rbp + 0x4f]
00949AE9  48 8B C8                        mov rcx, rax
00949AEC  48 89 45 5F                     mov qword ptr [rbp + 0x5f], rax
00949AF0  41 8B D7                        mov edx, r15d
00949AF3  E8 68 E5 AD FF                  call 0x140428060
00949AF8  84 C0                           test al, al
00949AFA  0F 84 7D 01 00 00               je 0x140949c7d
00949B00  48 8B 45 5F                     mov rax, qword ptr [rbp + 0x5f]
00949B04  8B 4D 4F                        mov ecx, dword ptr [rbp + 0x4f]
00949B07  48 03 C9                        add rcx, rcx
00949B0A  48 8B 80 60 07 00 00            mov rax, qword ptr [rax + 0x760]
00949B11  48 8B 44 C8 08                  mov rax, qword ptr [rax + rcx*8 + 8]
00949B16  49 89 44 24 58                  mov qword ptr [r12 + 0x58], rax
00949B1B  83 65 67 00                     and dword ptr [rbp + 0x67], 0
00949B1F  E9 15 FE FF FF                  jmp 0x140949939
00949B24  E8 87 B1 F0 FF                  call 0x140854cb0
00949B29  E9 04 FF FF FF                  jmp 0x140949a32
00949B2E  41 BF 01 00 00 00               mov r15d, 1
00949B34  E9 03 FD FF FF                  jmp 0x14094983c
00949B39  E8 E2 30 F1 FF                  call 0x14085cc20
00949B3E  E9 84 FE FF FF                  jmp 0x1409499c7
00949B43  E8 D8 30 F1 FF                  call 0x14085cc20
00949B48  E9 61 FE FF FF                  jmp 0x1409499ae
00949B4D  E8 CE 30 F1 FF                  call 0x14085cc20
00949B52  E9 39 FE FF FF                  jmp 0x140949990
00949B57  44 8B 7D CB                     mov r15d, dword ptr [rbp - 0x35]
00949B5B  44 89 7D 67                     mov dword ptr [rbp + 0x67], r15d
00949B5F  4D 85 F6                        test r14, r14
00949B62  75 57                           jne 0x140949bbb
00949B64  41 8B 55 04                     mov edx, dword ptr [r13 + 4]
00949B68  45 33 C9                        xor r9d, r9d
00949B6B  45 33 C0                        xor r8d, r8d
00949B6E  48 8B CF                        mov rcx, rdi
00949B71  E8 0A E5 F0 FF                  call 0x140858080
00949B76  8B F0                           mov esi, eax
00949B78  85 C0                           test eax, eax
00949B7A  0F 88 B5 FD FF FF               js 0x140949935
00949B80  45 8B C4                        mov r8d, r12d
00949B83  48 8B D7                        mov rdx, rdi
00949B86  49 8B CD                        mov rcx, r13
00949B89  E8 7A CA B8 FF                  call 0x1404d6608
00949B8E  8B F0                           mov esi, eax
00949B90  85 C0                           test eax, eax
00949B92  0F 88 9D FD FF FF               js 0x140949935
00949B98  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00949B9F  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00949BA3  41 8B 55 04                     mov edx, dword ptr [r13 + 4]
00949BA7  48 8B CF                        mov rcx, rdi
00949BAA  0F 84 9C C0 1D 00               je 0x140b25c4c
00949BB0  E8 AB B0 F0 FF                  call 0x140854c60
00949BB5  90                              nop
00949BB6  E9 96 C0 1D 00                  jmp 0x140b25c51
00949BBB  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00949BBF  45 89 7E 08                     mov dword ptr [r14 + 8], r15d
00949BC3  45 89 7E 04                     mov dword ptr [r14 + 4], r15d
00949BC7  8B 45 5F                        mov eax, dword ptr [rbp + 0x5f]
00949BCA  49 8D 4E 14                     lea rcx, [r14 + 0x14]
00949BCE  66 41 C7 06 73 6B               mov word ptr [r14], 0x6b73
00949BD4  44 8B C0                        mov r8d, eax
00949BD7  41 C7 46 0C 01 00 00 00         mov dword ptr [r14 + 0xc], 1
00949BDF  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
00949BE3  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
00949BE7  E8 54 CC D7 FF                  call 0x1406c6840
00949BEC  45 33 C0                        xor r8d, r8d
00949BEF  41 8B D7                        mov edx, r15d
00949BF2  48 8B CF                        mov rcx, rdi
00949BF5  E8 2E 46 02 00                  call 0x14096e228
00949BFA  33 C9                           xor ecx, ecx
00949BFC  8B F0                           mov esi, eax
00949BFE  85 C0                           test eax, eax
00949C00  0F 88 66 01 00 00               js 0x140949d6c
00949C06  48 39 4D 7F                     cmp qword ptr [rbp + 0x7f], rcx
00949C0A  0F 85 7E 01 00 00               jne 0x140949d8e
00949C10  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00949C14  45 8B C4                        mov r8d, r12d
00949C17  48 8B D7                        mov rdx, rdi
00949C1A  49 8B CD                        mov rcx, r13
00949C1D  44 89 78 2C                     mov dword ptr [rax + 0x2c], r15d
00949C21  E8 B6 CB B5 FF                  call 0x1404a67dc
00949C26  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00949C2D  48 8D 55 97                     lea rdx, [rbp - 0x69]
00949C31  44 8A F8                        mov r15b, al
00949C34  48 8B CF                        mov rcx, rdi
00949C37  75 36                           jne 0x140949c6f
00949C39  E8 02 C3 F0 FF                  call 0x140855f40
00949C3E  45 33 ED                        xor r13d, r13d
00949C41  45 84 FF                        test r15b, r15b
00949C44  0F 84 68 FE FF FF               je 0x140949ab2
00949C4A  41 8B D4                        mov edx, r12d
00949C4D  48 8B CF                        mov rcx, rdi
00949C50  E8 A7 25 B7 FF                  call 0x1404bc1fc
00949C55  41 8B D4                        mov edx, r12d
00949C58  48 8B CF                        mov rcx, rdi
00949C5B  E8 CC 0A F1 FF                  call 0x14085a72c
00949C60  E9 4D FE FF FF                  jmp 0x140949ab2
00949C65  E8 B6 2F F1 FF                  call 0x14085cc20
00949C6A  E9 1B FE FF FF                  jmp 0x140949a8a
00949C6F  E8 AC 2F F1 FF                  call 0x14085cc20
00949C74  EB C8                           jmp 0x140949c3e
00949C76  33 C0                           xor eax, eax
00949C78  E9 99 FE FF FF                  jmp 0x140949b16
00949C7D  49 83 64 24 58 00               and qword ptr [r12 + 0x58], 0
00949C83  BA 04 00 00 00                  mov edx, 4
00949C88  4D 8B CC                        mov r9, r12
00949C8B  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00949C90  8D 4A 4D                        lea ecx, [rdx + 0x4d]
00949C93  44 8D 42 FD                     lea r8d, [rdx - 3]
00949C97  E8 C4 39 BB FF                  call 0x1404fd660
00949C9C  CC                              int3
00949C9D  B8 9A 00 00 C0                  mov eax, 0xc000009a
00949CA2  E9 22 FD FF FF                  jmp 0x1409499c9
00949CA7  BE 9A 00 00 C0                  mov esi, 0xc000009a
00949CAC  49 8B DE                        mov rbx, r14
00949CAF  E9 89 FC FF FF                  jmp 0x14094993d
00949CB4  4C 21 75 9F                     and qword ptr [rbp - 0x61], r14
00949CB8  49 8B DE                        mov rbx, r14
00949CBB  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
00949CBF  E9 92 FC FF FF                  jmp 0x140949956
00949CC4  41 8B D4                        mov edx, r12d
00949CC7  E8 B4 E3 F0 FF                  call 0x140858080
00949CCC  8B F0                           mov esi, eax
00949CCE  85 C0                           test eax, eax
00949CD0  0F 88 5F FC FF FF               js 0x140949935
00949CD6  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
00949CDD  83 48 60 FF                     or dword ptr [rax + 0x60], 0xffffffff
00949CE1  48 83 60 58 00                  and qword ptr [rax + 0x58], 0
00949CE6  C7 40 44 09 00 00 00            mov dword ptr [rax + 0x44], 9
00949CED  C6 40 64 00                     mov byte ptr [rax + 0x64], 0
00949CF1  E9 92 FB FF FF                  jmp 0x140949888
00949CF6  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00949CFA  4C 8B 65 4F                     mov r12, qword ptr [rbp + 0x4f]
00949CFE  48 89 58 04                     mov qword ptr [rax + 4], rbx
00949D02  49 89 9C 24 A8 00 00 00         mov qword ptr [r12 + 0xa8], rbx
00949D0A  E9 26 FC FF FF                  jmp 0x140949935
00949D0F  45 8B C4                        mov r8d, r12d
00949D12  48 8B D7                        mov rdx, rdi
00949D15  49 8B CD                        mov rcx, r13
00949D18  E8 EB C8 B8 FF                  call 0x1404d6608
00949D1D  8B F0                           mov esi, eax
00949D1F  85 C0                           test eax, eax
00949D21  0F 88 0E FC FF FF               js 0x140949935
00949D27  E9 EA FC FF FF                  jmp 0x140949a16
00949D2C  48 83 7D 7F 00                  cmp qword ptr [rbp + 0x7f], 0
00949D31  0F 85 0B BF 1D 00               jne 0x140b25c42
00949D37  BA 04 00 00 00                  mov edx, 4
00949D3C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00949D41  4C 8B CF                        mov r9, rdi
00949D44  8D 4A 4D                        lea ecx, [rdx + 0x4d]
00949D47  44 8D 42 01                     lea r8d, [rdx + 1]
00949D4B  E8 10 39 BB FF                  call 0x1404fd660
00949D50  CC                              int3
00949D51  41 8B D4                        mov edx, r12d
00949D54  48 8B CF                        mov rcx, rdi
00949D57  E8 A0 24 B7 FF                  call 0x1404bc1fc
00949D5C  41 8B D4                        mov edx, r12d
00949D5F  48 8B CF                        mov rcx, rdi
00949D62  E8 C5 09 F1 FF                  call 0x14085a72c
00949D67  E9 2B FD FF FF                  jmp 0x140949a97
00949D6C  48 8B 5D 8F                     mov rbx, qword ptr [rbp - 0x71]
00949D70  48 39 4D 7F                     cmp qword ptr [rbp + 0x7f], rcx
00949D74  0F 85 C3 FB FF FF               jne 0x14094993d
00949D7A  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00949D7E  41 89 45 04                     mov dword ptr [r13 + 4], eax
00949D82  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00949D86  89 43 08                        mov dword ptr [rbx + 8], eax
00949D89  E9 AF FB FF FF                  jmp 0x14094993d
00949D8E  89 4D 5F                        mov dword ptr [rbp + 0x5f], ecx
00949D91  4C 8D 45 5F                     lea r8, [rbp + 0x5f]
00949D95  48 8B CF                        mov rcx, rdi
00949D98  41 8B D7                        mov edx, r15d
00949D9B  E8 C0 E2 AD FF                  call 0x140428060
00949DA0  84 C0                           test al, al
00949DA2  0F 85 D2 BE 1D 00               jne 0x140b25c7a
00949DA8  4C 8B 4D 4F                     mov r9, qword ptr [rbp + 0x4f]
00949DAC  BA 04 00 00 00                  mov edx, 4
00949DB1  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00949DB6  8D 4A 4D                        lea ecx, [rdx + 0x4d]
00949DB9  44 8D 42 FF                     lea r8d, [rdx - 1]
00949DBD  E8 9E 38 BB FF                  call 0x1404fd660
00949DC2  CC                              int3
00949DC3  48 8B 8D 87 00 00 00            mov rcx, qword ptr [rbp + 0x87]
00949DCA  E9 CD BE 1D 00                  jmp 0x140b25c9c
00949DCF  8B D0                           mov edx, eax
00949DD1  48 8B CF                        mov rcx, rdi
00949DD4  E8 53 09 F1 FF                  call 0x14085a72c
00949DD9  E9 8B FB FF FF                  jmp 0x140949969
00949DDE  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00949DE5  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00949DE9  48 8B CF                        mov rcx, rdi
00949DEC  0F 84 1D BF 1D 00               je 0x140b25d0f
00949DF2  E8 29 2E F1 FF                  call 0x14085cc20
00949DF7  E9 76 FB FF FF                  jmp 0x140949972
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpSetSecurityDescriptorInfo(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (184);
    v_r12 = 0;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rsp - 71 - 97) = 0;
    *(unsigned int *)(v_rsp - 71 - 105) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_rsp - 71 - 17) = v_xmm0;
    *(unsigned int *)(v_rsp - 71 - 89) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 73) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 65) = (unsigned int)(a1);
    *(unsigned int *)(v_rsp - 71 - 57) = 0;
    *(unsigned int *)(v_rsp - 71 - 53) = 0;
    *(unsigned int *)(v_rsp - 71 + 103) = 0;
    *(unsigned int *)(v_rsp - 71 - 101) = 0;
    *(unsigned int *)(v_rsp - 71 - 85) = 0;
    *(unsigned int *)(v_rsp - 71 - 69) = 0;
    *(unsigned int *)(v_rsp - 71 - 61) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 25) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 113) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 81) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 41) = 0;
    *(unsigned int *)(v_rsp - 71 - 33) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_009498EA;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))), v_rsp - 71 - 65, a4);
loc_0094972C:
    *(unsigned __int64 *)(v_rsp - 71 - 49) = result;
    if (result == 0) goto loc_00949C9D;
    result = CmpUpdateKeyNodeAccessBits(*(unsigned __int64 *)(a1 + 32), result, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))), a4);
    result = CmGetKCBCacheSecurity(a1, *(unsigned __int64 *)(v_rsp - 71 + 127), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))), a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_009498F4;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result)))), v_rsp - 71 - 105, a4);
loc_00949772:
    if (result == 0) goto loc_00949CA7;
    result = CmpAllocatePool(256, (unsigned int)(*(unsigned int *)(result + 16)), (unsigned int)(0x36384D43ULL), a4);
    *(unsigned __int64 *)(v_rsp - 71 - 41) = result;
    if (result == 0) goto loc_00949CA7;
    result = memcpy(result, result + 20, (unsigned int)(*(unsigned int *)(result + 16)), a4);
    *(unsigned __int64 *)(v_rsp - 71 - 97) = *(unsigned __int64 *)(v_rsp - 71 - 41);
    a1 = 0;
    v_stack_mC0 = *(unsigned __int64 *)(v_rsp - 71 + 143);
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 71 + 119);
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 111)));
    result = RtlpSetSecurityObject(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 87))), a3, v_rsp - 71 - 97);
    if (sign_flag) goto loc_00949CB4;
    v_stack_mD8 = *(unsigned __int64 *)(v_rsp - 71 - 97);
    result = CmpTraceSecurityChanging(0, *(unsigned __int64 *)(v_rsp - 71 - 41), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 87))), *(unsigned __int64 *)(v_rsp - 71 + 95));
    if (sign_flag) goto loc_00949CAC;
    result = RtlLengthSecurityDescriptorStrict(*(unsigned __int64 *)(v_rsp - 71 - 97), *(unsigned __int64 *)(v_rsp - 71 - 41), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 87))), *(unsigned __int64 *)(v_rsp - 71 + 95));
    *(unsigned int *)(v_rsp - 71 + 95) = (unsigned int)(result);
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) != 0) goto loc_00949B2E;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) >> (31));
loc_0094983C:
    a4 = 0;
    a3 = 0;
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) != 0) goto loc_00949CC4;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(v_rsp - 71 - 33)), a3, a4);
    if (sign_flag) goto loc_00949935;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result)))), a3, a4);
    if (sign_flag) goto loc_00949935;
loc_00949888:
    v_stack_mD8 = v_rsp - 71 - 25;
    result = CmpFindMatchingDescriptorCell(*(unsigned __int64 *)(a1 + 32), *(unsigned __int64 *)(v_rsp - 71 - 97), (unsigned int)((unsigned int)(v_r15)), v_rsp - 71 - 57);
    if ((unsigned __int8)(result) == 0) goto loc_009498FE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) goto loc_009499DE;
    if (*(unsigned __int64 *)(v_rsp - 71 + 127) == 0) goto loc_00949CF6;
    a4 = 0;
    result = CmpKeySecurityIncrementReferenceCount(result, *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), a4);
    if (sign_flag) goto loc_00949935;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 135) + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 135) + 88) = *(unsigned __int64 *)(v_rsp - 71 - 25);
    goto loc_00949935;
loc_009498EA:
    result = HvpGetCellPaged(result, *(unsigned __int64 *)(v_rsp - 71 + 135), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), a4);
    goto loc_0094972C;
loc_009498F4:
    result = HvpGetCellPaged(result, *(unsigned __int64 *)(v_rsp - 71 + 135), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), a4);
    goto loc_00949772;
loc_009498FE:
    result = RtlLengthSecurityDescriptorStrict(*(unsigned __int64 *)(v_rsp - 71 - 97), *(unsigned __int64 *)(v_rsp - 71 + 135), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), a4);
    v_stack_mD0 = v_rsp - 71 - 89;
    v_stack_mD8 = v_rsp - 71 - 81;
    result = HvAllocateCell(*(unsigned __int64 *)(a1 + 32), result + 20, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 53);
    if (!sign_flag) goto loc_00949B57;
loc_00949935:
loc_00949939:
loc_0094993D:
    if (*(unsigned __int64 *)(v_rsp - 71 - 97) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 71 - 97), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 53);
    }
    result = *(unsigned __int64 *)(v_rsp - 71 - 41);
    if (*(unsigned __int64 *)(v_rsp - 71 - 41) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 41);
        result = CmSiFreeMemory(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 53);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103))) != 0) goto loc_00949DCF;
loc_00949969:
    if (*(unsigned __int64 *)(v_rsp - 71 - 113) != 0) goto loc_00949DDE;
loc_00949972:
    if (*(unsigned __int64 *)(v_rsp - 71 - 81) == 0) goto loc_00949990;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) != 0) goto loc_00949B4D;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_rsp - 71 - 89, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 53);
loc_00949990:
    if (result == 0) goto loc_009499AE;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) != 0) goto loc_00949B43;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_rsp - 71 - 105, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 53);
loc_009499AE:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) != 0) goto loc_00949B39;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_rsp - 71 - 65, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 53);
loc_009499C7:
loc_009499C9:
    v_rsp = (v_rsp) + (184);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_009499DE:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), a3, a4);
    if (sign_flag) goto loc_00949935;
    if (*(unsigned __int64 *)(v_rsp - 71 - 81) == 0) goto loc_00949D0F;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 135) + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 25))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 135) + 88) = *(unsigned __int64 *)(v_rsp - 71 - 25);
loc_00949A16:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) == 0) goto loc_00949B24;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 89, a4);
loc_00949A32:
    if (result == 0) goto loc_00949D2C;
    a4 = 0;
    result = CmpKeySecurityIncrementReferenceCount(result, *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), a4);
    if (sign_flag) goto loc_00949939;
    if ((*(unsigned __int64 *)(v_rsp - 71 + 127)) != 0) goto loc_00949A9F;
    result = CmpKeySecurityDecrementReferenceCount(result, *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result)))), a4);
    *(unsigned __int8 *)(v_rsp - 71 + 95) = (unsigned __int8)(result);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) != 0) goto loc_00949C65;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_rsp - 71 - 105, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result)))), a4);
loc_00949A8A:
    v_r13 = 0;
    if ((*(unsigned __int8 *)(v_rsp - 71 + 95)) != 0) goto loc_00949D51;
loc_00949A97:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)));
loc_00949A9F:
    if ((*(unsigned __int64 *)(v_rsp - 71 + 127)) != 0) goto loc_00949DC3;
loc_00949AB2:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 4) = *(unsigned __int64 *)(v_rsp - 71 - 113);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 168) = *(unsigned __int64 *)(v_rsp - 71 - 113);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 44)))) == -1) goto loc_00949C76;
    *(unsigned __int64 *)(v_rsp - 71 + 95) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32);
    result = CmpFindSecurityCellCacheIndex(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 44)))), v_rsp - 71 + 79, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00949C7D;
    a1 = ((unsigned int)(*(unsigned int *)(v_rsp - 71 + 79))) + ((unsigned int)(*(unsigned int *)(v_rsp - 71 + 79)));
loc_00949B16:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 95) + 1888) + a1 * 8 + 8);
    goto loc_00949939;
loc_00949B24:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 44)))), v_rsp - 71 + 79, a4);
    goto loc_00949A32;
loc_00949B2E:
    goto loc_0094983C;
loc_00949B39:
    result = HvpReleaseCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 44)))), v_rsp - 71 + 79, a4);
    goto loc_009499C7;
loc_00949B43:
    result = HvpReleaseCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 44)))), v_rsp - 71 + 79, a4);
    goto loc_009499AE;
loc_00949B4D:
    result = HvpReleaseCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 44)))), v_rsp - 71 + 79, a4);
    goto loc_00949990;
loc_00949B57:
    *(unsigned int *)(v_rsp - 71 + 103) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 53)));
    if (result != 0) goto loc_00949BBB;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(v_r13 + 4)), a3, a4);
    if (sign_flag) goto loc_00949935;
    result = CmpKeySecurityMarkDirtyForReferenceCountDecrement(0, *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), a4);
    if (sign_flag) goto loc_00949935;
    result = HvpGetCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)(*(unsigned int *)(v_r13 + 4)), v_rsp - 71 - 73, a4);
loc_00949BBB:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 53)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81) + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 53)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 71 - 81)) = 0x6B73ULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81) + 12) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)));
    result = memcpy(*(unsigned __int64 *)(v_rsp - 71 - 81) + 20, *(unsigned __int64 *)(v_rsp - 71 - 97), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)))), a4);
    a3 = 0;
    result = CmpAddSecurityCellToCache(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 53)))), a3, a4);
    a1 = 0;
    if (sign_flag) goto loc_00949D6C;
    if ((*(unsigned __int64 *)(v_rsp - 71 + 127)) != 0) goto loc_00949D8E;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 53)));
    result = CmpKeySecurityDecrementReferenceCount(0, *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140)) & (1)) != 0) goto loc_00949C6F;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(a1 + 32), v_rsp - 71 - 105, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), a4);
loc_00949C3E:
    v_r13 = 0;
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00949AB2;
    result = CmpRemoveSecurityCellList(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), a4);
    result = HvFreeCell(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), a4);
    goto loc_00949AB2;
loc_00949C65:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), a4);
    goto loc_00949A8A;
loc_00949C6F:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), a4);
    goto loc_00949C3E;
loc_00949C76:
    result = 0;
    goto loc_00949B16;
loc_00949C7D:
    v_stack_p20 = (unsigned __int8)(result);
    result = KeBugCheckEx(4 + 77, 4, 4 - 3, *(unsigned __int64 *)(v_rsp - 71 + 79));
loc_00949C9D:
    goto loc_009499C9;
loc_00949CA7:
loc_00949CAC:
    goto loc_0094993D;
loc_00949CB4:
    goto loc_00949956;
loc_00949CC4:
    result = HvpMarkCellDirty(4 + 77, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), 4 - 3, *(unsigned __int64 *)(v_rsp - 71 + 79));
    if (sign_flag) goto loc_00949935;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 135) + 68) = 9;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 71 + 135) + 100) = 0;
    goto loc_00949888;
loc_00949CF6:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 4) = *(unsigned __int64 *)(v_rsp - 71 - 81);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 168) = *(unsigned __int64 *)(v_rsp - 71 - 81);
    goto loc_00949935;
loc_00949D0F:
    result = CmpKeySecurityMarkDirtyForReferenceCountDecrement(0, *(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), *(unsigned __int64 *)(v_rsp - 71 + 79));
    if (sign_flag) goto loc_00949935;
    goto loc_00949A16;
loc_00949D2C:
    v_stack_p20 = (unsigned __int8)(result);
    result = KeBugCheckEx(4 + 77, 4, 4 + 1, *(unsigned __int64 *)(a1 + 32));
loc_00949D51:
    result = CmpRemoveSecurityCellList(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), 4 + 1, *(unsigned __int64 *)(a1 + 32));
    result = HvFreeCell(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79))), 4 + 1, *(unsigned __int64 *)(a1 + 32));
    goto loc_00949A97;
loc_00949D6C:
    if ((*(unsigned __int64 *)(v_rsp - 71 + 127)) != (*(unsigned __int64 *)(a1 + 32))) goto loc_0094993D;
    *(unsigned int *)(v_r13 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81) + 4)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 113) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 81) + 8)));
    goto loc_0094993D;
loc_00949D8E:
    *(unsigned int *)(v_rsp - 71 + 95) = (unsigned int)(*(unsigned __int64 *)(a1 + 32));
    result = CmpFindSecurityCellCacheIndex(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)((unsigned __int8)(result))), v_rsp - 71 + 95, *(unsigned __int64 *)(a1 + 32));
    v_stack_p20 = (unsigned __int8)(result);
    result = KeBugCheckEx(4 + 77, 4, 4 - 1, *(unsigned __int64 *)(v_rsp - 71 + 79));
loc_00949DC3:
loc_00949DCF:
    result = HvFreeCell(*(unsigned __int64 *)(a1 + 32), (unsigned int)((unsigned int)(result)), 4 - 1, *(unsigned __int64 *)(v_rsp - 71 + 79));
    goto loc_00949969;
loc_00949DDE:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(a1 + 32), v_rsp - 71 - 73, 4 - 1, *(unsigned __int64 *)(v_rsp - 71 + 79));
    goto loc_00949972;
}
```

## 5. (Beta) C Style

```c
int64_t CmpSetSecurityDescriptorInfo(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (184);
    local_r12 = 0;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    *(uint64_t *)(local_rsp - 0x47 - 0x61) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x69) = (uint32_t)(Arg1);
    *(uint64_t *)(local_rsp - 0x47 - 0x11) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x47 - 0x59) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x49) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x41) = (uint32_t)(Arg1);
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = 0;
    *(uint32_t *)(local_rsp - 0x47 + 0x67) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x65) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x55) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x45) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x3D) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x19) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x71) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x51) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_009498EA;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))), local_rsp - 71 - 65, Arg4);
loc_0094972C:
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = result;
    if (result == 0) goto loc_00949C9D;
    result = CmpUpdateKeyNodeAccessBits(*(uint64_t *)(arg1 + 0x20), result, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))), Arg4);
    result = CmGetKCBCacheSecurity(Arg1, *(uint64_t *)(local_rsp - 0x47 + 0x7F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))), Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_009498F4;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result)))), local_rsp - 71 - 105, Arg4);
loc_00949772:
    if (result == 0) goto loc_00949CA7;
    result = CmpAllocatePool(256, (uint32_t)(*(uint32_t *)(result + 0x10)), (uint32_t)(0x36384D43ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = result;
    if (result == 0) goto loc_00949CA7;
    result = memcpy(result, result + 20, (uint32_t)(*(uint32_t *)(result + 0x10)), Arg4);
    *(uint64_t *)(local_rsp - 0x47 - 0x61) = *(uint64_t *)(local_rsp - 0x47 - 0x29);
    Arg1 = 0;
    v_stack_mC0 = *(uint64_t *)(local_rsp - 0x47 + 0x8F);
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x47 + 0x77);
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x6F)));
    result = RtlpSetSecurityObject(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57))), Arg3, local_rsp - 71 - 97);
    if (sign_flag) goto loc_00949CB4;
    v_stack_mD8 = *(uint64_t *)(local_rsp - 0x47 - 0x61);
    result = CmpTraceSecurityChanging(0, *(uint64_t *)(local_rsp - 0x47 - 0x29), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57))), *(uint64_t *)(local_rsp - 0x47 + 0x5F));
    if (sign_flag) goto loc_00949CAC;
    result = RtlLengthSecurityDescriptorStrict(*(uint64_t *)(local_rsp - 0x47 - 0x61), *(uint64_t *)(local_rsp - 0x47 - 0x29), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57))), *(uint64_t *)(local_rsp - 0x47 + 0x5F));
    *(uint32_t *)(local_rsp - 0x47 + 0x5F) = (uint32_t)(result);
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) != 0) goto loc_00949B2E;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) >> (31));
loc_0094983C:
    Arg4 = 0;
    Arg3 = 0;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) != 0) goto loc_00949CC4;
    result = HvpMarkCellDirty(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x21)), Arg3, Arg4);
    if (sign_flag) goto loc_00949935;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result)))), Arg3, Arg4);
    if (sign_flag) goto loc_00949935;
loc_00949888:
    v_stack_mD8 = local_rsp - 71 - 25;
    result = CmpFindMatchingDescriptorCell(*(uint64_t *)(arg1 + 0x20), *(uint64_t *)(local_rsp - 0x47 - 0x61), (uint32_t)((uint32_t)(local_r15)), local_rsp - 71 - 57);
    if ((uint8_t)(result) == 0) goto loc_009498FE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) goto loc_009499DE;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x7F) == 0) goto loc_00949CF6;
    Arg4 = 0;
    result = CmpKeySecurityIncrementReferenceCount(result, *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), Arg4);
    if (sign_flag) goto loc_00949935;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x87) + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x87) + 0x58) = *(uint64_t *)(local_rsp - 0x47 - 0x19);
    goto loc_00949935;
loc_009498EA:
    result = HvpGetCellPaged(result, *(uint64_t *)(local_rsp - 0x47 + 0x87), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), Arg4);
    goto loc_0094972C;
loc_009498F4:
    result = HvpGetCellPaged(result, *(uint64_t *)(local_rsp - 0x47 + 0x87), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), Arg4);
    goto loc_00949772;
loc_009498FE:
    result = RtlLengthSecurityDescriptorStrict(*(uint64_t *)(local_rsp - 0x47 - 0x61), *(uint64_t *)(local_rsp - 0x47 + 0x87), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), Arg4);
    v_stack_mD0 = local_rsp - 71 - 89;
    v_stack_mD8 = local_rsp - 71 - 81;
    result = HvAllocateCell(*(uint64_t *)(arg1 + 0x20), result + 20, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 53);
    if (!sign_flag) goto loc_00949B57;
loc_00949935:
loc_00949939:
loc_0094993D:
    if (*(uint64_t *)(local_rsp - 0x47 - 0x61) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x47 - 0x61), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 53);
    }
    result = *(uint64_t *)(local_rsp - 0x47 - 0x29);
    if (*(uint64_t *)(local_rsp - 0x47 - 0x29) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x29);
        result = CmSiFreeMemory(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 53);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67))) != 0) goto loc_00949DCF;
loc_00949969:
    if (*(uint64_t *)(local_rsp - 0x47 - 0x71) != 0) goto loc_00949DDE;
loc_00949972:
    if (*(uint64_t *)(local_rsp - 0x47 - 0x51) == 0) goto loc_00949990;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00949B4D;
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), local_rsp - 71 - 89, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 53);
loc_00949990:
    if (result == 0) goto loc_009499AE;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00949B43;
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), local_rsp - 71 - 105, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 53);
loc_009499AE:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00949B39;
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), local_rsp - 71 - 65, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 53);
loc_009499C7:
loc_009499C9:
    local_rsp = (local_rsp) + (184);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_009499DE:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), Arg3, Arg4);
    if (sign_flag) goto loc_00949935;
    if (*(uint64_t *)(local_rsp - 0x47 - 0x51) == 0) goto loc_00949D0F;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x87) + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x19))));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x87) + 0x58) = *(uint64_t *)(local_rsp - 0x47 - 0x19);
loc_00949A16:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) == 0) goto loc_00949B24;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 89, Arg4);
loc_00949A32:
    if (result == 0) goto loc_00949D2C;
    Arg4 = 0;
    result = CmpKeySecurityIncrementReferenceCount(result, *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), Arg4);
    if (sign_flag) goto loc_00949939;
    if ((*(uint64_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_00949A9F;
    result = CmpKeySecurityDecrementReferenceCount(result, *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result)))), Arg4);
    *(uint8_t *)(local_rsp - 0x47 + 0x5F) = (uint8_t)(result);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00949C65;
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), local_rsp - 71 - 105, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result)))), Arg4);
loc_00949A8A:
    local_r13 = 0;
    if ((*(uint8_t *)(local_rsp - 0x47 + 0x5F)) != 0) goto loc_00949D51;
loc_00949A97:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)));
loc_00949A9F:
    if ((*(uint64_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_00949DC3;
loc_00949AB2:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x4) = *(uint64_t *)(local_rsp - 0x47 - 0x71);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0xA8) = *(uint64_t *)(local_rsp - 0x47 - 0x71);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x2C)))) == -1) goto loc_00949C76;
    *(uint64_t *)(local_rsp - 0x47 + 0x5F) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20);
    result = CmpFindSecurityCellCacheIndex(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x2C)))), local_rsp - 71 + 79, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00949C7D;
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x4F))) + ((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x4F)));
loc_00949B16:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x5F) + 0x760) + arg1 * 8 + 0x8);
    goto loc_00949939;
loc_00949B24:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x2C)))), local_rsp - 71 + 79, Arg4);
    goto loc_00949A32;
loc_00949B2E:
    goto loc_0094983C;
loc_00949B39:
    result = HvpReleaseCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x2C)))), local_rsp - 71 + 79, Arg4);
    goto loc_009499C7;
loc_00949B43:
    result = HvpReleaseCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x2C)))), local_rsp - 71 + 79, Arg4);
    goto loc_009499AE;
loc_00949B4D:
    result = HvpReleaseCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x2C)))), local_rsp - 71 + 79, Arg4);
    goto loc_00949990;
loc_00949B57:
    *(uint32_t *)(local_rsp - 0x47 + 0x67) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35)));
    if (result != 0) goto loc_00949BBB;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(local_r13 + 0x4)), Arg3, Arg4);
    if (sign_flag) goto loc_00949935;
    result = CmpKeySecurityMarkDirtyForReferenceCountDecrement(0, *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), Arg4);
    if (sign_flag) goto loc_00949935;
    result = HvpGetCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)(*(uint32_t *)(local_r13 + 0x4)), local_rsp - 71 - 73, Arg4);
loc_00949BBB:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35)));
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51)) = 0x6B73ULL;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 0xC) = 1;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)));
    result = memcpy(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 20, *(uint64_t *)(local_rsp - 0x47 - 0x61), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)))), Arg4);
    Arg3 = 0;
    result = CmpAddSecurityCellToCache(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35)))), Arg3, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00949D6C;
    if ((*(uint64_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_00949D8E;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35)));
    result = CmpKeySecurityDecrementReferenceCount(0, *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00949C6F;
    result = HvpReleaseCellPaged(*(uint64_t *)(arg1 + 0x20), local_rsp - 71 - 105, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), Arg4);
loc_00949C3E:
    local_r13 = 0;
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00949AB2;
    result = CmpRemoveSecurityCellList(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), Arg4);
    result = HvFreeCell(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), Arg4);
    goto loc_00949AB2;
loc_00949C65:
    result = HvpReleaseCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), Arg4);
    goto loc_00949A8A;
loc_00949C6F:
    result = HvpReleaseCellFlat(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), Arg4);
    goto loc_00949C3E;
loc_00949C76:
    result = 0;
    goto loc_00949B16;
loc_00949C7D:
    v_stack_p20 = (uint8_t)(result);
    result = KeBugCheckEx(4 + 77, 4, 4 - 3, *(uint64_t *)(local_rsp - 0x47 + 0x4F));
loc_00949C9D:
    goto loc_009499C9;
loc_00949CA7:
loc_00949CAC:
    goto loc_0094993D;
loc_00949CB4:
    goto loc_00949956;
loc_00949CC4:
    result = HvpMarkCellDirty(4 + 77, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), 4 - 3, *(uint64_t *)(local_rsp - 0x47 + 0x4F));
    if (sign_flag) goto loc_00949935;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x87) + 0x44) = 9;
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x87) + 0x64) = 0;
    goto loc_00949888;
loc_00949CF6:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x4) = *(uint64_t *)(local_rsp - 0x47 - 0x51);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0xA8) = *(uint64_t *)(local_rsp - 0x47 - 0x51);
    goto loc_00949935;
loc_00949D0F:
    result = CmpKeySecurityMarkDirtyForReferenceCountDecrement(0, *(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), *(uint64_t *)(local_rsp - 0x47 + 0x4F));
    if (sign_flag) goto loc_00949935;
    goto loc_00949A16;
loc_00949D2C:
    v_stack_p20 = (uint8_t)(result);
    result = KeBugCheckEx(4 + 77, 4, 4 + 1, *(uint64_t *)(arg1 + 0x20));
loc_00949D51:
    result = CmpRemoveSecurityCellList(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), 4 + 1, *(uint64_t *)(arg1 + 0x20));
    result = HvFreeCell(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F))), 4 + 1, *(uint64_t *)(arg1 + 0x20));
    goto loc_00949A97;
loc_00949D6C:
    if ((*(uint64_t *)(local_rsp - 0x47 + 0x7F)) != (*(uint64_t *)(arg1 + 0x20))) goto loc_0094993D;
    *(uint32_t *)(local_r13 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 0x4)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x71) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x51) + 0x8)));
    goto loc_0094993D;
loc_00949D8E:
    *(uint32_t *)(local_rsp - 0x47 + 0x5F) = (uint32_t)(*(uint64_t *)(arg1 + 0x20));
    result = CmpFindSecurityCellCacheIndex(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)((uint8_t)(result))), local_rsp - 71 + 95, *(uint64_t *)(arg1 + 0x20));
    v_stack_p20 = (uint8_t)(result);
    result = KeBugCheckEx(4 + 77, 4, 4 - 1, *(uint64_t *)(local_rsp - 0x47 + 0x4F));
loc_00949DC3:
loc_00949DCF:
    result = HvFreeCell(*(uint64_t *)(arg1 + 0x20), (uint32_t)((uint32_t)(result)), 4 - 1, *(uint64_t *)(local_rsp - 0x47 + 0x4F));
    goto loc_00949969;
loc_00949DDE:
    result = HvpReleaseCellFlat(*(uint64_t *)(arg1 + 0x20), local_rsp - 71 - 73, 4 - 1, *(uint64_t *)(local_rsp - 0x47 + 0x4F));
    goto loc_00949972;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00949688&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
