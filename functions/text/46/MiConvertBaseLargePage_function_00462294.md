# MiConvertBaseLargePage

- RVA: `0x00462294`–`0x004622ED` (길이 `89` bytes)
- VA: `0x0000000140462294`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `23`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiLargePagePromote](../37/MiLargePagePromote_function_0037915C.md) at `0x00379418`
- [MiConvertLargePfnToSmall](../42/MiConvertLargePfnToSmall_function_00420CA0.md) at `0x00420E19`
- [MiTryUnlinkNodeLargePages](../68/MiTryUnlinkNodeLargePages_function_0068ADA0.md) at `0x0068AF5A`
- [sub_006E7436](../6E/Unknown_function_006E7436.md) at `0x006E74BD`
- [sub_006E798E](../6E/Unknown_function_006E798E.md) at `0x006E79C9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00462294  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00462298  45 33 C0                        xor r8d, r8d
0046229B  85 D2                           test edx, edx
0046229D  74 2E                           je 0x1404622cd
0046229F  48 BA 01 00 00 00 00 00 00 C0   movabs rdx, 0xc000000000000001
004622A9  48 23 C2                        and rax, rdx
004622AC  48 83 C8 01                     or rax, 1
004622B0  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
004622B4  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
004622B7  89 44 24 10                     mov dword ptr [rsp + 0x10], eax
004622BB  41 8D 40 02                     lea eax, [r8 + 2]
004622BF  66 89 44 24 10                  mov word ptr [rsp + 0x10], ax
004622C4  8B 44 24 10                     mov eax, dword ptr [rsp + 0x10]
004622C8  89 41 20                        mov dword ptr [rcx + 0x20], eax
004622CB  C3                              ret
004622CC  CC                              int3
004622CD  48 BA 00 00 00 00 00 00 00 C0   movabs rdx, 0xc000000000000000
004622D7  48 23 C2                        and rax, rdx
004622DA  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
004622DE  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
004622E1  89 44 24 10                     mov dword ptr [rsp + 0x10], eax
004622E5  66 44 89 44 24 10               mov word ptr [rsp + 0x10], r8w
004622EB  EB D7                           jmp 0x1404622c4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiConvertBaseLargePage(__int64 a1, int a2, int a3)
{
    __int64 result;
    unsigned int v_stack_p10;

    a3 = 0;
    if (a2 == 0) goto loc_004622CD;
    result = (*(unsigned __int64 *)(a1 + 24)) & (a2);
    result = (result) | (1);
    *(unsigned __int64 *)(a1 + 24) = result;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    v_stack_p10 = (unsigned __int16)(a3 + 2);
loc_004622C4:
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p10));
    return (unsigned int)(v_stack_p10);
loc_004622CD:
    result = ((unsigned int)(v_stack_p10)) & (a2);
    *(unsigned __int64 *)(a1 + 24) = result;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    v_stack_p10 = 0;
    goto loc_004622C4;
}
```

## 5. (Beta) C Style

```c
int64_t MiConvertBaseLargePage(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    uint32_t v_stack_p10;

    Arg3 = 0;
    if (Arg2 == 0) goto loc_004622CD;
    result = (*(uint64_t *)(arg1 + 0x18)) & (Arg2);
    result = (result) | (1);
    *(uint64_t *)(arg1 + 0x18) = result;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    v_stack_p10 = (uint16_t)(Arg3 + 2);
loc_004622C4:
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p10));
    return (uint32_t)(v_stack_p10);
loc_004622CD:
    result = ((uint32_t)(v_stack_p10)) & (Arg2);
    *(uint64_t *)(arg1 + 0x18) = result;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    v_stack_p10 = 0;
    goto loc_004622C4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00462294&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00462294[BB_00462294]
  bb_0046229F[BB_0046229F]
  bb_004622C4[BB_004622C4]
  bb_004622CC[BB_004622CC]
  bb_004622CD[BB_004622CD]
  bb_00462294 -->|branch| bb_004622CD
  bb_00462294 -->|fallthrough| bb_0046229F
  bb_0046229F -->|flow| bb_004622C4
  bb_004622CC -->|flow| bb_004622CD
  bb_004622CD -->|branch| bb_004622C4
```
