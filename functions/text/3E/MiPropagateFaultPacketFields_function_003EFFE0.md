# MiPropagateFaultPacketFields

- RVA: `0x003EFFE0`–`0x003F0063` (길이 `131` bytes)
- VA: `0x00000001403EFFE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `32`개 명령, `131/131` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiInPagePageTable](MiInPagePageTable_function_003EF8DC.md) at `0x003EFBF2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EFFE0  48 83 EC 28                     sub rsp, 0x28
003EFFE4  0F 10 51 38                     movups xmm2, xmmword ptr [rcx + 0x38]
003EFFE8  4C 8B C1                        mov r8, rcx
003EFFEB  0F 10 42 38                     movups xmm0, xmmword ptr [rdx + 0x38]
003EFFEF  66 0F 73 DA 08                  psrldq xmm2, 8
003EFFF4  0F 11 41 38                     movups xmmword ptr [rcx + 0x38], xmm0
003EFFF8  F2 0F 10 4A 48                  movsd xmm1, qword ptr [rdx + 0x48]
003EFFFD  F2 0F 11 49 48                  movsd qword ptr [rcx + 0x48], xmm1
003F0002  66 48 0F 7E D1                  movq rcx, xmm2
003F0007  48 C1 E9 28                     shr rcx, 0x28
003F000B  0F B6 C1                        movzx eax, cl
003F000E  32 42 45                        xor al, byte ptr [rdx + 0x45]
003F0011  24 03                           and al, 3
003F0013  32 C1                           xor al, cl
003F0015  41 88 40 45                     mov byte ptr [r8 + 0x45], al
003F0019  48 8B 42 78                     mov rax, qword ptr [rdx + 0x78]
003F001D  49 89 40 78                     mov qword ptr [r8 + 0x78], rax
003F0021  48 8B 82 80 00 00 00            mov rax, qword ptr [rdx + 0x80]
003F0028  49 89 80 80 00 00 00            mov qword ptr [r8 + 0x80], rax
003F002F  48 8B 82 90 00 00 00            mov rax, qword ptr [rdx + 0x90]
003F0036  49 89 80 90 00 00 00            mov qword ptr [r8 + 0x90], rax
003F003D  48 8B 82 88 00 00 00            mov rax, qword ptr [rdx + 0x88]
003F0044  49 89 80 88 00 00 00            mov qword ptr [r8 + 0x88], rax
003F004B  41 8B 40 50                     mov eax, dword ptr [r8 + 0x50]
003F004F  8B C8                           mov ecx, eax
003F0051  33 4A 50                        xor ecx, dword ptr [rdx + 0x50]
003F0054  83 E1 1F                        and ecx, 0x1f
003F0057  33 C8                           xor ecx, eax
003F0059  41 89 48 50                     mov dword ptr [r8 + 0x50], ecx
003F005D  48 83 C4 28                     add rsp, 0x28
003F0061  C3                              ret
003F0062  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPropagateFaultPacketFields(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(a1 + 56) = v_xmm0;
    *(unsigned __int64 *)(a1 + 72) = v_xmm1;
    a1 = (a1) >> (40);
    result = (unsigned __int8)(((unsigned __int8)(a1)) ^ (*(unsigned __int8 *)(a2 + 69)));
    result = (unsigned __int8)((result) & (3));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(a1 + 69) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a1 + 120) = *(unsigned __int64 *)(a2 + 120);
    *(unsigned __int64 *)(a1 + 128) = *(unsigned __int64 *)(a2 + 128);
    *(unsigned __int64 *)(a1 + 144) = *(unsigned __int64 *)(a2 + 144);
    *(unsigned __int64 *)(a1 + 136) = *(unsigned __int64 *)(a2 + 136);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 80))))) ^ (*(unsigned int *)(a2 + 80)));
    a1 = (unsigned int)((a1) & (31));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 80)))));
    *(unsigned int *)(a1 + 80) = (unsigned int)(a1);
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(a1 + 80));
}
```

## 5. (Beta) C Style

```c
int64_t MiPropagateFaultPacketFields(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(arg1 + 0x38) = v_xmm0;
    *(uint64_t *)(arg1 + 0x48) = v_xmm1;
    Arg1 = (Arg1) >> (40);
    result = (uint8_t)(((uint8_t)(Arg1)) ^ (*(uint8_t *)(arg2 + 0x45)));
    result = (uint8_t)((result) & (3));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    *(uint8_t *)(arg1 + 0x45) = (uint8_t)(result);
    *(uint64_t *)(arg1 + 0x78) = *(uint64_t *)(arg2 + 0x78);
    *(uint64_t *)(arg1 + 0x80) = *(uint64_t *)(arg2 + 0x80);
    *(uint64_t *)(arg1 + 0x90) = *(uint64_t *)(arg2 + 0x90);
    *(uint64_t *)(arg1 + 0x88) = *(uint64_t *)(arg2 + 0x88);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50))))) ^ (*(uint32_t *)(arg2 + 0x50)));
    Arg1 = (uint32_t)((Arg1) & (31));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))));
    *(uint32_t *)(arg1 + 0x50) = (uint32_t)(Arg1);
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(arg1 + 0x50));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `128` | `R` |
| `Arg1` | `+ 0x45` | `8` | `W` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `W` |
| `Arg1` | `+ 0x78` | `64` | `W` |
| `Arg1` | `+ 0x80` | `64` | `W` |
| `Arg1` | `+ 0x88` | `64` | `W` |
| `Arg1` | `+ 0x90` | `64` | `W` |
| `Arg2` | `+ 0x38` | `128` | `R` |
| `Arg2` | `+ 0x45` | `8` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg2` | `+ 0x50` | `32` | `R` |
| `Arg2` | `+ 0x78` | `64` | `R` |
| `Arg2` | `+ 0x80` | `64` | `R` |
| `Arg2` | `+ 0x88` | `64` | `R` |
| `Arg2` | `+ 0x90` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EFFE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EFFE0[BB_003EFFE0]
  bb_003F0062[BB_003F0062]
```
