# RtlCompressBufferXpressHuff

- RVA: `0x0026B9A0`–`0x0026BA55` (길이 `181` bytes)
- VA: `0x000000014026B9A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065538`
- 디코드: `47`개 명령, `181/181` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0026B9F8` → [RtlCompressBufferXpressHuffStandard](RtlCompressBufferXpressHuffStandard_function_0026BA60.md) (function, `0x0026BA60`)
- `0x0026BA42` → [RtlCompressBufferXpressHuffMax](RtlCompressBufferXpressHuffMax_function_0026CA10.md) (function, `0x0026CA10`)

### Direct callers
- [SmStoreCompressBuffer](SmStoreCompressBuffer_function_002683E0.md) at `0x0026851F`
- [RtlCompressBuffer](RtlCompressBuffer_function_0026A220.md) at `0x0026A337`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0026B9A0  40 53                           push rbx
0026B9A2  48 83 EC 50                     sub rsp, 0x50
0026B9A6  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0026B9AE  4D 8B D9                        mov r11, r9
0026B9B1  48 83 C0 07                     add rax, 7
0026B9B5  45 8B D0                        mov r10d, r8d
0026B9B8  48 83 E0 F8                     and rax, 0xfffffffffffffff8
0026B9BC  48 8B DA                        mov rbx, rdx
0026B9BF  66 85 C9                        test cx, cx
0026B9C2  75 40                           jne 0x14026ba04
0026B9C4  44 8B 8C 24 80 00 00 00         mov r9d, dword ptr [rsp + 0x80]
0026B9CC  33 C9                           xor ecx, ecx
0026B9CE  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
0026B9D3  41 8B D2                        mov edx, r10d
0026B9D6  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0026B9DB  4D 8B C3                        mov r8, r11
0026B9DE  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0026B9E3  48 8B CB                        mov rcx, rbx
0026B9E6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0026B9EB  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0026B9F3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0026B9F8  E8 63 00 00 00                  call 0x14026ba60
0026B9FD  48 83 C4 50                     add rsp, 0x50
0026BA01  5B                              pop rbx
0026BA02  C3                              ret
0026BA03  CC                              int3
0026BA04  BA 00 01 00 00                  mov edx, 0x100
0026BA09  66 3B CA                        cmp cx, dx
0026BA0C  75 40                           jne 0x14026ba4e
0026BA0E  44 8B 8C 24 80 00 00 00         mov r9d, dword ptr [rsp + 0x80]
0026BA16  33 C9                           xor ecx, ecx
0026BA18  44 89 54 24 40                  mov dword ptr [rsp + 0x40], r10d
0026BA1D  4D 8B C3                        mov r8, r11
0026BA20  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0026BA25  41 8B D2                        mov edx, r10d
0026BA28  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0026BA2D  48 8B CB                        mov rcx, rbx
0026BA30  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0026BA35  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0026BA3D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0026BA42  E8 C9 0F 00 00                  call 0x14026ca10
0026BA47  48 83 C4 50                     add rsp, 0x50
0026BA4B  5B                              pop rbx
0026BA4C  C3                              ret
0026BA4D  CC                              int3
0026BA4E  B8 BB 00 00 C0                  mov eax, 0xc00000bb
0026BA53  EB A8                           jmp 0x14026b9fd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlCompressBufferXpressHuff(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;

    v_rsp = (v_rsp) - (80);
    result = (a8) + (7);
    result = (result) & (-8);
    if ((unsigned __int16)(a1) != 0) goto loc_0026BA04;
    a1 = 0;
    v_stack_m18 = a3;
    v_stack_m20 = 0;
    v_stack_m28 = 0;
    v_stack_m30 = result;
    v_stack_m38 = a7;
    result = RtlCompressBufferXpressHuffStandard(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4, (unsigned int)(a5));
loc_0026B9FD:
    v_rsp = (v_rsp) + (80);
    return result;
loc_0026BA04:
    if (((unsigned __int16)(a2)) != 256) goto loc_0026BA4E;
    a1 = 0;
    v_stack_p40 = (unsigned int)((unsigned int)(a3));
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = result;
    v_stack_p20 = a7;
    result = RtlCompressBufferXpressHuffMax(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4, (unsigned int)(a5));
    v_rsp = (v_rsp) + (80);
    return result;
loc_0026BA4E:
    goto loc_0026B9FD;
}
```

## 5. (Beta) C Style

```c
int64_t RtlCompressBufferXpressHuff(int32_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint64_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;

    local_rsp = (local_rsp) - (80);
    result = (Arg8) + (7);
    result = (result) & (-8);
    if ((uint16_t)(Arg1) != 0) goto loc_0026BA04;
    Arg1 = 0;
    v_stack_m18 = Arg3;
    v_stack_m20 = 0;
    v_stack_m28 = 0;
    v_stack_m30 = result;
    v_stack_m38 = Arg7;
    result = RtlCompressBufferXpressHuffStandard(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4, (uint32_t)(Arg5));
loc_0026B9FD:
    local_rsp = (local_rsp) + (80);
    return result;
loc_0026BA04:
    if (((uint16_t)(Arg2)) != 256) goto loc_0026BA4E;
    Arg1 = 0;
    v_stack_p40 = (uint32_t)((uint32_t)(Arg3));
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = result;
    v_stack_p20 = Arg7;
    result = RtlCompressBufferXpressHuffMax(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4, (uint32_t)(Arg5));
    local_rsp = (local_rsp) + (80);
    return result;
loc_0026BA4E:
    goto loc_0026B9FD;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026B9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0026B9A0[BB_0026B9A0]
  bb_0026B9C4[BB_0026B9C4]
  bb_0026B9FD[BB_0026B9FD]
  bb_0026BA03[BB_0026BA03]
  bb_0026BA04[BB_0026BA04]
  bb_0026BA0E[BB_0026BA0E]
  bb_0026BA4D[BB_0026BA4D]
  bb_0026BA4E[BB_0026BA4E]
  bb_0026B9A0 -->|branch| bb_0026BA04
  bb_0026B9A0 -->|fallthrough| bb_0026B9C4
  bb_0026B9C4 -->|flow| bb_0026B9FD
  bb_0026BA03 -->|flow| bb_0026BA04
  bb_0026BA04 -->|branch| bb_0026BA4E
  bb_0026BA04 -->|fallthrough| bb_0026BA0E
  bb_0026BA4D -->|flow| bb_0026BA4E
  bb_0026BA4E -->|branch| bb_0026B9FD
```
