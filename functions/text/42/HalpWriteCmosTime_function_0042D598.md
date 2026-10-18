# HalpWriteCmosTime

- RVA: `0x0042D598`–`0x0042D78C` (길이 `500` bytes)
- VA: `0x000000014042D598`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `202`개 명령, `500/500` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0042D5AF` → [HalpAcquireCmosSpinLockAndWait](HalpAcquireCmosSpinLockAndWait_function_0042DE20.md) (function, `0x0042DE20`)
- `0x0042D735` → [HalpSetCmosCenturyByte](HalpSetCmosCenturyByte_function_0042E97C.md) (function, `0x0042E97C`)
- `0x0042D771` → [HalpReleaseCmosSpinLock](HalpReleaseCmosSpinLock_function_0042DE04.md) (function, `0x0042DE04`)

### Direct callers
- [HalSetRealTimeClock](HalSetRealTimeClock_function_0042D310.md) at `0x0042D390`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0042D598  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0042D59D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0042D5A2  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0042D5A7  57                              push rdi
0042D5A8  48 83 EC 20                     sub rsp, 0x20
0042D5AC  48 8B D9                        mov rbx, rcx
0042D5AF  E8 6C 08 00 00                  call 0x14042de20
0042D5B4  44 0F B6 43 0A                  movzx r8d, byte ptr [rbx + 0xa]
0042D5B9  33 C0                           xor eax, eax
0042D5BB  90                              nop
0042D5BC  BD CD CC CC CC                  mov ebp, 0xcccccccd
0042D5C1  45 8B C8                        mov r9d, r8d
0042D5C4  BF 70 00 00 00                  mov edi, 0x70
0042D5C9  8B D7                           mov edx, edi
0042D5CB  EE                              out dx, al
0042D5CC  90                              nop
0042D5CD  8B C5                           mov eax, ebp
0042D5CF  41 F7 E0                        mul r8d
0042D5D2  90                              nop
0042D5D3  8D 77 01                        lea esi, [rdi + 1]
0042D5D6  8B CA                           mov ecx, edx
0042D5D8  8B C5                           mov eax, ebp
0042D5DA  41 F7 E0                        mul r8d
0042D5DD  C1 E9 03                        shr ecx, 3
0042D5E0  C1 EA 03                        shr edx, 3
0042D5E3  C0 E1 04                        shl cl, 4
0042D5E6  8D 04 92                        lea eax, [rdx + rdx*4]
0042D5E9  8B D6                           mov edx, esi
0042D5EB  03 C0                           add eax, eax
0042D5ED  44 2B C8                        sub r9d, eax
0042D5F0  41 8D 04 09                     lea eax, [r9 + rcx]
0042D5F4  EE                              out dx, al
0042D5F5  90                              nop
0042D5F6  8B D7                           mov edx, edi
0042D5F8  0F B6 4B 08                     movzx ecx, byte ptr [rbx + 8]
0042D5FC  B0 02                           mov al, 2
0042D5FE  90                              nop
0042D5FF  44 8B C1                        mov r8d, ecx
0042D602  EE                              out dx, al
0042D603  90                              nop
0042D604  8B C5                           mov eax, ebp
0042D606  F7 E1                           mul ecx
0042D608  90                              nop
0042D609  8B C5                           mov eax, ebp
0042D60B  8B CA                           mov ecx, edx
0042D60D  41 F7 E0                        mul r8d
0042D610  C1 E9 03                        shr ecx, 3
0042D613  C1 EA 03                        shr edx, 3
0042D616  C0 E1 04                        shl cl, 4
0042D619  8D 04 92                        lea eax, [rdx + rdx*4]
0042D61C  8B D6                           mov edx, esi
0042D61E  03 C0                           add eax, eax
0042D620  44 2B C0                        sub r8d, eax
0042D623  41 8D 04 08                     lea eax, [r8 + rcx]
0042D627  EE                              out dx, al
0042D628  90                              nop
0042D629  8B D7                           mov edx, edi
0042D62B  0F B6 4B 06                     movzx ecx, byte ptr [rbx + 6]
0042D62F  B0 04                           mov al, 4
0042D631  90                              nop
0042D632  44 8B C1                        mov r8d, ecx
0042D635  EE                              out dx, al
0042D636  90                              nop
0042D637  8B C5                           mov eax, ebp
0042D639  F7 E1                           mul ecx
0042D63B  90                              nop
0042D63C  8B C5                           mov eax, ebp
0042D63E  8B CA                           mov ecx, edx
0042D640  41 F7 E0                        mul r8d
0042D643  C1 E9 03                        shr ecx, 3
0042D646  C1 EA 03                        shr edx, 3
0042D649  C0 E1 04                        shl cl, 4
0042D64C  8D 04 92                        lea eax, [rdx + rdx*4]
0042D64F  8B D6                           mov edx, esi
0042D651  03 C0                           add eax, eax
0042D653  44 2B C0                        sub r8d, eax
0042D656  41 8D 04 08                     lea eax, [r8 + rcx]
0042D65A  EE                              out dx, al
0042D65B  90                              nop
0042D65C  8B D7                           mov edx, edi
0042D65E  0F B6 4B 0E                     movzx ecx, byte ptr [rbx + 0xe]
0042D662  B0 06                           mov al, 6
0042D664  90                              nop
0042D665  EE                              out dx, al
0042D666  90                              nop
0042D667  90                              nop
0042D668  44 8B C1                        mov r8d, ecx
0042D66B  8B C5                           mov eax, ebp
0042D66D  F7 E1                           mul ecx
0042D66F  8B C5                           mov eax, ebp
0042D671  8B CA                           mov ecx, edx
0042D673  41 F7 E0                        mul r8d
0042D676  C1 E9 03                        shr ecx, 3
0042D679  C1 EA 03                        shr edx, 3
0042D67C  C0 E1 04                        shl cl, 4
0042D67F  8D 04 92                        lea eax, [rdx + rdx*4]
0042D682  8B D6                           mov edx, esi
0042D684  03 C0                           add eax, eax
0042D686  44 2B C0                        sub r8d, eax
0042D689  41 8D 04 08                     lea eax, [r8 + rcx]
0042D68D  EE                              out dx, al
0042D68E  90                              nop
0042D68F  8B D7                           mov edx, edi
0042D691  0F B6 4B 04                     movzx ecx, byte ptr [rbx + 4]
0042D695  B0 07                           mov al, 7
0042D697  90                              nop
0042D698  44 8B C1                        mov r8d, ecx
0042D69B  EE                              out dx, al
0042D69C  90                              nop
0042D69D  8B C5                           mov eax, ebp
0042D69F  F7 E1                           mul ecx
0042D6A1  90                              nop
0042D6A2  8B C5                           mov eax, ebp
0042D6A4  8B CA                           mov ecx, edx
0042D6A6  41 F7 E0                        mul r8d
0042D6A9  C1 E9 03                        shr ecx, 3
0042D6AC  C1 EA 03                        shr edx, 3
0042D6AF  C0 E1 04                        shl cl, 4
0042D6B2  8D 04 92                        lea eax, [rdx + rdx*4]
0042D6B5  8B D6                           mov edx, esi
0042D6B7  03 C0                           add eax, eax
0042D6B9  44 2B C0                        sub r8d, eax
0042D6BC  41 8D 04 08                     lea eax, [r8 + rcx]
0042D6C0  EE                              out dx, al
0042D6C1  90                              nop
0042D6C2  8B D7                           mov edx, edi
0042D6C4  0F B6 4B 02                     movzx ecx, byte ptr [rbx + 2]
0042D6C8  B0 08                           mov al, 8
0042D6CA  44 8B C1                        mov r8d, ecx
0042D6CD  90                              nop
0042D6CE  EE                              out dx, al
0042D6CF  90                              nop
0042D6D0  8B C5                           mov eax, ebp
0042D6D2  F7 E1                           mul ecx
0042D6D4  90                              nop
0042D6D5  8B C5                           mov eax, ebp
0042D6D7  8B CA                           mov ecx, edx
0042D6D9  41 F7 E0                        mul r8d
0042D6DC  C1 E9 03                        shr ecx, 3
0042D6DF  C1 EA 03                        shr edx, 3
0042D6E2  C0 E1 04                        shl cl, 4
0042D6E5  8D 04 92                        lea eax, [rdx + rdx*4]
0042D6E8  8B D6                           mov edx, esi
0042D6EA  03 C0                           add eax, eax
0042D6EC  44 2B C0                        sub r8d, eax
0042D6EF  41 8D 04 08                     lea eax, [r8 + rcx]
0042D6F3  EE                              out dx, al
0042D6F4  B8 0F 27 00 00                  mov eax, 0x270f
0042D6F9  90                              nop
0042D6FA  0F BF 1B                        movsx ebx, word ptr [rbx]
0042D6FD  3B D8                           cmp ebx, eax
0042D6FF  0F 47 D8                        cmova ebx, eax
0042D702  B8 1F 85 EB 51                  mov eax, 0x51eb851f
0042D707  F7 E3                           mul ebx
0042D709  8B C5                           mov eax, ebp
0042D70B  C1 EA 05                        shr edx, 5
0042D70E  44 0F B6 DA                     movzx r11d, dl
0042D712  41 F7 E3                        mul r11d
0042D715  8B C5                           mov eax, ebp
0042D717  41 8B CB                        mov ecx, r11d
0042D71A  44 8B C2                        mov r8d, edx
0042D71D  41 F7 E3                        mul r11d
0042D720  41 C1 E8 03                     shr r8d, 3
0042D724  C1 EA 03                        shr edx, 3
0042D727  41 C0 E0 04                     shl r8b, 4
0042D72B  8D 04 92                        lea eax, [rdx + rdx*4]
0042D72E  03 C0                           add eax, eax
0042D730  2B C8                           sub ecx, eax
0042D732  41 02 C8                        add cl, r8b
0042D735  E8 42 12 00 00                  call 0x14042e97c
0042D73A  90                              nop
0042D73B  B0 09                           mov al, 9
0042D73D  8B D7                           mov edx, edi
0042D73F  EE                              out dx, al
0042D740  41 6B D3 64                     imul edx, r11d, 0x64
0042D744  90                              nop
0042D745  90                              nop
0042D746  8B C5                           mov eax, ebp
0042D748  2A DA                           sub bl, dl
0042D74A  44 0F B6 C3                     movzx r8d, bl
0042D74E  41 F7 E0                        mul r8d
0042D751  8B C5                           mov eax, ebp
0042D753  8B CA                           mov ecx, edx
0042D755  41 F7 E0                        mul r8d
0042D758  C1 E9 03                        shr ecx, 3
0042D75B  C1 EA 03                        shr edx, 3
0042D75E  C0 E1 04                        shl cl, 4
0042D761  8D 04 92                        lea eax, [rdx + rdx*4]
0042D764  8B D6                           mov edx, esi
0042D766  03 C0                           add eax, eax
0042D768  44 2B C0                        sub r8d, eax
0042D76B  41 8D 04 08                     lea eax, [r8 + rcx]
0042D76F  EE                              out dx, al
0042D770  90                              nop
0042D771  E8 8E 06 00 00                  call 0x14042de04
0042D776  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0042D77B  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0042D780  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0042D785  48 83 C4 20                     add rsp, 0x20
0042D789  5F                              pop rdi
0042D78A  C3                              ret
0042D78B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpWriteCmosTime(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = HalpAcquireCmosSpinLockAndWait(a1, a2, a3, a4);
    result = 0;
    a1 = (unsigned int)((112) >> (3));
    a2 = (unsigned int)((112) >> (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned int)((a2 + a2 * 4) + ((unsigned int)(a2 + a2 * 4)));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 10)))) - ((unsigned int)(result)));
    a1 = (unsigned int)((112) >> (3));
    a2 = (unsigned int)((112) >> (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned int)((a2 + a2 * 4) + ((unsigned int)(a2 + a2 * 4)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 8)))) - ((unsigned int)(result)));
    a1 = (unsigned int)((112) >> (3));
    a2 = (unsigned int)((112) >> (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned int)((a2 + a2 * 4) + ((unsigned int)(a2 + a2 * 4)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 6)))) - ((unsigned int)(result)));
    a1 = (unsigned int)((112) >> (3));
    a2 = (unsigned int)((112) >> (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned int)((a2 + a2 * 4) + ((unsigned int)(a2 + a2 * 4)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 14)))) - ((unsigned int)(result)));
    a1 = (unsigned int)((112) >> (3));
    a2 = (unsigned int)((112) >> (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned int)((a2 + a2 * 4) + ((unsigned int)(a2 + a2 * 4)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 4)))) - ((unsigned int)(result)));
    a1 = (unsigned int)((112) >> (3));
    a2 = (unsigned int)((112) >> (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned int)((a2 + a2 * 4) + ((unsigned int)(a2 + a2 * 4)));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 2)))) - ((unsigned int)(result)));
    v_rbx = (__int16)(*(unsigned __int16 *)(a1));
    if (((unsigned int)((__int16)(*(unsigned __int16 *)(a1)))) > ((unsigned int)((unsigned int)(0x270FULL)))) { v_rbx = (unsigned int)((unsigned int)(0x270FULL)); }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(112 + 1))) >> (5));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a2))) >> (3));
    a2 = (unsigned int)((a2) >> (3));
    a3 = (unsigned __int8)((a3) << (4));
    result = (unsigned int)((a2 + a2 * 4) + ((unsigned int)(a2 + a2 * 4)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(a2)))) - ((unsigned int)(result)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a3)));
    result = HalpSetCmosCenturyByte(a1, a2, a3, a4);
    a2 = (unsigned int)((112) * ((unsigned int)((unsigned __int8)(a2))));
    v_rbx = (unsigned __int8)((v_rbx) - ((unsigned __int8)(a2)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) >> (3));
    a2 = (unsigned int)((a2) >> (3));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned int)((a2 + a2 * 4) + ((unsigned int)(a2 + a2 * 4)));
    a3 = (unsigned int)(((unsigned __int8)(v_rbx)) - ((unsigned int)(result)));
    result = HalpReleaseCmosSpinLock(a1, (unsigned int)((unsigned int)(112 + 1)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpWriteCmosTime(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = HalpAcquireCmosSpinLockAndWait(Arg1, a2, a3, a4);
    result = 0;
    Arg1 = (uint32_t)((112) >> (3));
    a2 = (uint32_t)((112) >> (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint32_t)((a2 + a2 * 4) + ((uint32_t)(a2 + a2 * 4)));
    a4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0xA)))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((112) >> (3));
    a2 = (uint32_t)((112) >> (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint32_t)((a2 + a2 * 4) + ((uint32_t)(a2 + a2 * 4)));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x8)))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((112) >> (3));
    a2 = (uint32_t)((112) >> (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint32_t)((a2 + a2 * 4) + ((uint32_t)(a2 + a2 * 4)));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x6)))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((112) >> (3));
    a2 = (uint32_t)((112) >> (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint32_t)((a2 + a2 * 4) + ((uint32_t)(a2 + a2 * 4)));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0xE)))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((112) >> (3));
    a2 = (uint32_t)((112) >> (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint32_t)((a2 + a2 * 4) + ((uint32_t)(a2 + a2 * 4)));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x4)))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((112) >> (3));
    a2 = (uint32_t)((112) >> (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint32_t)((a2 + a2 * 4) + ((uint32_t)(a2 + a2 * 4)));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x2)))) - ((uint32_t)(result)));
    local_rbx = (int16_t)(*(uint16_t *)(arg1));
    if (((uint32_t)((int16_t)(*(uint16_t *)(arg1)))) > ((uint32_t)((uint32_t)(0x270FULL)))) { local_rbx = (uint32_t)((uint32_t)(0x270FULL)); }
    a2 = (uint32_t)(((uint32_t)((uint32_t)(112 + 1))) >> (5));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(a2))) >> (3));
    a2 = (uint32_t)((a2) >> (3));
    a3 = (uint8_t)((a3) << (4));
    result = (uint32_t)((a2 + a2 * 4) + ((uint32_t)(a2 + a2 * 4)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(a2)))) - ((uint32_t)(result)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(a3)));
    result = HalpSetCmosCenturyByte(Arg1, a2, a3, a4);
    a2 = (uint32_t)((112) * ((uint32_t)((uint8_t)(a2))));
    local_rbx = (uint8_t)((local_rbx) - ((uint8_t)(a2)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(a2))) >> (3));
    a2 = (uint32_t)((a2) >> (3));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint32_t)((a2 + a2 * 4) + ((uint32_t)(a2 + a2 * 4)));
    a3 = (uint32_t)(((uint8_t)(local_rbx)) - ((uint32_t)(result)));
    result = HalpReleaseCmosSpinLock(Arg1, (uint32_t)((uint32_t)(112 + 1)), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x6` | `8` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0xA` | `8` | `R` |
| `Arg1` | `+ 0xE` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042D598&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042D598[BB_0042D598]
  bb_0042D78B[BB_0042D78B]
```
