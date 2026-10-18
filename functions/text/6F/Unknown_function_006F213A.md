# sub_006F213A

- RVA: `0x006F213A`–`0x006F23AC` (길이 `626` bytes)
- VA: `0x00000001406F213A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9B18`
- 디코드: `137`개 명령, `626/626` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F21B5` → [PsIsCurrentThreadInServerSilo](../43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x006F21BE` → [PsGetCurrentServerSiloGlobals](../2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x006F222D` → [PsIsCurrentThreadInServerSilo](../43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x006F2236` → [PsGetCurrentServerSiloGlobals](../2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **22**
  - `0x006F2175` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F218A` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F21A6` → [RtlGetSystemGlobalData + 0x30](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F21AF` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F21E0` → [RtlGetSystemGlobalData + 0x30](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F21E9` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F21FF` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F221E` → [RtlGetSystemGlobalData + 0x30](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2227` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2273` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F22B7` → [RtlGetSystemGlobalData + 0x30](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F22F4` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2307` → [RtlGetSystemGlobalData + 0x2D](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2311` → [RtlGetSystemGlobalData + 0x32](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F231A` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2329` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2341` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2350` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2368` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F237D` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F2396` → [RtlGetSystemGlobalData + 0x4B](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)
  - `0x006F23A7` → [RtlGetSystemGlobalData + 0x30](../45/RtlGetSystemGlobalData_function_0045F710.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F213A  83 E9 01                        sub ecx, 1
006F213D  0F 84 2C 01 00 00               je 0x1406f226f
006F2143  83 E9 01                        sub ecx, 1
006F2146  0F 84 D7 00 00 00               je 0x1406f2223
006F214C  83 E9 01                        sub ecx, 1
006F214F  0F 84 A6 00 00 00               je 0x1406f21fb
006F2155  83 E9 01                        sub ecx, 1
006F2158  0F 84 87 00 00 00               je 0x1406f21e5
006F215E  83 E9 01                        sub ecx, 1
006F2161  74 48                           je 0x1406f21ab
006F2163  83 E9 01                        sub ecx, 1
006F2166  74 1E                           je 0x1406f2186
006F2168  83 F9 01                        cmp ecx, 1
006F216B  0F 85 9B 01 00 00               jne 0x1406f230c
006F2171  41 83 F8 04                     cmp r8d, 4
006F2175  0F 85 E0 D5 D6 FF               jne 0x14045f75b
006F217B  A1 70 02 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff78000000270]
006F2184  EB 1E                           jmp 0x1406f21a4
006F2186  41 83 F8 04                     cmp r8d, 4
006F218A  0F 85 CB D5 D6 FF               jne 0x14045f75b
006F2190  A1 6C 02 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff7800000026c]
006F2199  EB 09                           jmp 0x1406f21a4
006F219B  A1 F0 02 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000002f0]
006F21A4  89 02                           mov dword ptr [rdx], eax
006F21A6  E9 95 D5 D6 FF                  jmp 0x14045f740
006F21AB  41 83 F8 04                     cmp r8d, 4
006F21AF  0F 85 A6 D5 D6 FF               jne 0x14045f75b
006F21B5  E8 26 41 D4 FF                  call 0x1404362e0
006F21BA  84 C0                           test al, al
006F21BC  74 14                           je 0x1406f21d2
006F21BE  E8 2D C0 C0 FF                  call 0x1402fe1f0
006F21C3  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
006F21CA  48 05 48 02 00 00               add rax, 0x248
006F21D0  EB 0A                           jmp 0x1406f21dc
006F21D2  48 B8 40 02 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000240
006F21DC  8B 00                           mov eax, dword ptr [rax]
006F21DE  89 03                           mov dword ptr [rbx], eax
006F21E0  E9 5B D5 D6 FF                  jmp 0x14045f740
006F21E5  41 83 F8 02                     cmp r8d, 2
006F21E9  0F 85 6C D5 D6 FF               jne 0x14045f75b
006F21EF  66 A1 2E 00 00 00 80 F7 FF FF   movabs ax, word ptr [0xfffff7800000002e]
006F21F9  EB 20                           jmp 0x1406f221b
006F21FB  41 83 F8 02                     cmp r8d, 2
006F21FF  0F 85 56 D5 D6 FF               jne 0x14045f75b
006F2205  66 A1 2C 00 00 00 80 F7 FF FF   movabs ax, word ptr [0xfffff7800000002c]
006F220F  EB 0A                           jmp 0x1406f221b
006F2211  66 A1 C6 03 00 00 80 F7 FF FF   movabs ax, word ptr [0xfffff780000003c6]
006F221B  66 89 02                        mov word ptr [rdx], ax
006F221E  E9 1D D5 D6 FF                  jmp 0x14045f740
006F2223  41 83 F8 08                     cmp r8d, 8
006F2227  0F 85 2E D5 D6 FF               jne 0x14045f75b
006F222D  E8 AE 40 D4 FF                  call 0x1404362e0
006F2232  84 C0                           test al, al
006F2234  74 15                           je 0x1406f224b
006F2236  E8 B5 BF C0 FF                  call 0x1402fe1f0
006F223B  48 8B 90 08 05 00 00            mov rdx, qword ptr [rax + 0x508]
006F2242  48 81 C2 50 02 00 00            add rdx, 0x250
006F2249  EB 0E                           jmp 0x1406f2259
006F224B  48 BA 20 00 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000020
006F2255  EB 02                           jmp 0x1406f2259
006F2257  F3 90                           pause
006F2259  8B 4A 04                        mov ecx, dword ptr [rdx + 4]
006F225C  8B 02                           mov eax, dword ptr [rdx]
006F225E  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
006F2262  8B 42 08                        mov eax, dword ptr [rdx + 8]
006F2265  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
006F2269  3B C8                           cmp ecx, eax
006F226B  75 EA                           jne 0x1406f2257
006F226D  EB 40                           jmp 0x1406f22af
006F226F  41 83 F8 08                     cmp r8d, 8
006F2273  0F 85 E2 D4 D6 FF               jne 0x14045f75b
006F2279  48 BA 08 00 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000008
006F2283  49 B8 0C 00 00 00 80 F7 FF FF   movabs r8, 0xfffff7800000000c
006F228D  49 B9 10 00 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000010
006F2297  EB 02                           jmp 0x1406f229b
006F2299  F3 90                           pause
006F229B  41 8B 08                        mov ecx, dword ptr [r8]
006F229E  8B 02                           mov eax, dword ptr [rdx]
006F22A0  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
006F22A4  41 8B 01                        mov eax, dword ptr [r9]
006F22A7  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
006F22AB  3B C8                           cmp ecx, eax
006F22AD  75 EA                           jne 0x1406f2299
006F22AF  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
006F22B4  48 89 03                        mov qword ptr [rbx], rax
006F22B7  E9 84 D4 D6 FF                  jmp 0x14045f740
006F22BC  83 E9 0A                        sub ecx, 0xa
006F22BF  0F 84 CD 00 00 00               je 0x1406f2392
006F22C5  83 E9 01                        sub ecx, 1
006F22C8  0F 84 AB 00 00 00               je 0x1406f2379
006F22CE  83 E9 01                        sub ecx, 1
006F22D1  0F 84 8D 00 00 00               je 0x1406f2364
006F22D7  83 E9 01                        sub ecx, 1
006F22DA  74 70                           je 0x1406f234c
006F22DC  83 E9 01                        sub ecx, 1
006F22DF  74 5C                           je 0x1406f233d
006F22E1  83 E9 02                        sub ecx, 2
006F22E4  74 3F                           je 0x1406f2325
006F22E6  83 E9 01                        sub ecx, 1
006F22E9  74 2B                           je 0x1406f2316
006F22EB  83 F9 01                        cmp ecx, 1
006F22EE  75 1C                           jne 0x1406f230c
006F22F0  41 83 F8 08                     cmp r8d, 8
006F22F4  0F 85 61 D4 D6 FF               jne 0x14045f75b
006F22FA  48 B8 B8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003b8
006F2304  48 8B 00                        mov rax, qword ptr [rax]
006F2307  E9 31 D4 D6 FF                  jmp 0x14045f73d
006F230C  B8 0D 00 00 C0                  mov eax, 0xc000000d
006F2311  E9 2C D4 D6 FF                  jmp 0x14045f742
006F2316  41 83 F8 02                     cmp r8d, 2
006F231A  0F 85 3B D4 D6 FF               jne 0x14045f75b
006F2320  E9 EC FE FF FF                  jmp 0x1406f2211
006F2325  41 83 F8 01                     cmp r8d, 1
006F2329  0F 85 2C D4 D6 FF               jne 0x14045f75b
006F232F  48 B8 C6 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003c6
006F2339  8A 00                           mov al, byte ptr [rax]
006F233B  EB 68                           jmp 0x1406f23a5
006F233D  41 83 F8 04                     cmp r8d, 4
006F2341  0F 85 14 D4 D6 FF               jne 0x14045f75b
006F2347  E9 4F FE FF FF                  jmp 0x1406f219b
006F234C  41 83 F8 04                     cmp r8d, 4
006F2350  0F 85 05 D4 D6 FF               jne 0x14045f75b
006F2356  A1 E4 02 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000002e4]
006F235F  E9 40 FE FF FF                  jmp 0x1406f21a4
006F2364  41 83 F8 01                     cmp r8d, 1
006F2368  0F 85 ED D3 D6 FF               jne 0x14045f75b
006F236E  A0 EC 02 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff780000002ec]
006F2377  EB 2C                           jmp 0x1406f23a5
006F2379  41 83 F8 02                     cmp r8d, 2
006F237D  0F 85 D8 D3 D6 FF               jne 0x14045f75b
006F2383  66 A1 D6 02 00 00 80 F7 FF FF   movabs ax, word ptr [0xfffff780000002d6]
006F238D  E9 89 FE FF FF                  jmp 0x1406f221b
006F2392  41 83 F8 01                     cmp r8d, 1
006F2396  0F 85 BF D3 D6 FF               jne 0x14045f75b
006F239C  A0 D4 02 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff780000002d4]
006F23A5  88 02                           mov byte ptr [rdx], al
006F23A7  E9 94 D3 D6 FF                  jmp 0x14045f740
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F213A(int a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;

    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_006F226F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_006F2223;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_006F21FB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_006F21E5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_006F21AB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_006F2186;
    if (a1 != 1) goto loc_006F230C;
    goto loc_006F21A4;
loc_006F2186:
    goto loc_006F21A4;
loc_006F21A4:
    *(unsigned int *)(a2) = (unsigned int)(result);
loc_006F21AB:
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006F21D2;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    result = (*(unsigned __int64 *)(result + 1288)) + (584);
    goto loc_006F21DC;
loc_006F21D2:
loc_006F21DC:
    *(unsigned int *)(v_rbx) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
loc_006F21E5:
    goto loc_006F221B;
loc_006F21FB:
    goto loc_006F221B;
loc_006F221B:
    *(unsigned __int16 *)(a2) = (unsigned __int16)((unsigned int)(*(unsigned int *)(result)));
loc_006F2223:
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006F224B;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    a2 = (*(unsigned __int64 *)(result + 1288)) + (592);
    goto loc_006F2259;
loc_006F224B:
    goto loc_006F2259;
loc_006F2257:
loc_006F2259:
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    v_stack_p4C = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))))) goto loc_006F2257;
    goto loc_006F22AF;
loc_006F226F:
    goto loc_006F229B;
loc_006F2299:
loc_006F229B:
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    v_stack_p4C = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_006F2299;
loc_006F22AF:
    *(unsigned __int64 *)(v_rbx) = a9;
loc_006F230C:
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F213A(int32_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;

    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_006F226F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_006F2223;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_006F21FB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_006F21E5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_006F21AB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_006F2186;
    if (Arg1 != 1) goto loc_006F230C;
    goto loc_006F21A4;
loc_006F2186:
    goto loc_006F21A4;
loc_006F21A4:
    *(uint32_t *)(arg2) = (uint32_t)(result);
loc_006F21AB:
    result = PsIsCurrentThreadInServerSilo(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006F21D2;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    result = (*(uint64_t *)(result + 0x508)) + (584);
    goto loc_006F21DC;
loc_006F21D2:
loc_006F21DC:
    *(uint32_t *)(local_rbx) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
loc_006F21E5:
    goto loc_006F221B;
loc_006F21FB:
    goto loc_006F221B;
loc_006F221B:
    *(uint16_t *)(arg2) = (uint16_t)((uint32_t)(*(uint32_t *)(result)));
loc_006F2223:
    result = PsIsCurrentThreadInServerSilo(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006F224B;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    Arg2 = (*(uint64_t *)(result + 0x508)) + (592);
    goto loc_006F2259;
loc_006F224B:
    goto loc_006F2259;
loc_006F2257:
loc_006F2259:
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    v_stack_p4C = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8))))) goto loc_006F2257;
    goto loc_006F22AF;
loc_006F226F:
    goto loc_006F229B;
loc_006F2299:
loc_006F229B:
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    v_stack_p4C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_006F2299;
loc_006F22AF:
    *(uint64_t *)(local_rbx) = Arg9;
loc_006F230C:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `W` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F213A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
