# sub_00967B70

- RVA: `0x00967B70`–`0x00967BDB` (길이 `107` bytes)
- VA: `0x0000000140967B70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `28`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00967F18](Unknown_function_00967F18.md) at `0x0096850B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00967B70  4C 8B D9                        mov r11, rcx
00967B73  4C 8B D2                        mov r10, rdx
00967B76  48 B8 89 88 88 88 88 88 88 88   movabs rax, 0x8888888888888889
00967B80  41 83 E3 03                     and r11d, 3
00967B84  49 F7 E0                        mul r8
00967B87  48 C1 EA 03                     shr rdx, 3
00967B8B  0F B6 C2                        movzx eax, dl
00967B8E  44 6B C8 0F                     imul r9d, eax, 0xf
00967B92  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00967B9C  49 F7 E2                        mul r10
00967B9F  45 2A C1                        sub r8b, r9b
00967BA2  44 8B 4C 24 38                  mov r9d, dword ptr [rsp + 0x38]
00967BA7  48 D1 EA                        shr rdx, 1
00967BAA  49 03 D3                        add rdx, r11
00967BAD  41 8D 48 01                     lea ecx, [r8 + 1]
00967BB1  45 8B C1                        mov r8d, r9d
00967BB4  41 D3 E8                        shr r8d, cl
00967BB7  49 8D 4A 01                     lea rcx, [r10 + 1]
00967BBB  48 03 CA                        add rcx, rdx
00967BBE  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00967BC3  83 E1 03                        and ecx, 3
00967BC6  42 0F B7 04 5A                  movzx eax, word ptr [rdx + r11*2]
00967BCB  0F B7 0C 4A                     movzx ecx, word ptr [rdx + rcx*2]
00967BCF  44 2B C9                        sub r9d, ecx
00967BD2  41 0F AF C1                     imul eax, r9d
00967BD6  41 2B C0                        sub eax, r8d
00967BD9  C3                              ret
00967BDA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00967B70(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r11;

    v_r11 = (unsigned int)((a1) & (3));
    a2 = (a2) >> (3);
    a4 = (unsigned int)((a4) * ((unsigned int)((unsigned __int8)(a2))));
    a3 = (unsigned __int8)((a3) - ((unsigned __int8)(a4)));
    a2 = (a2) >> (1);
    a2 = (a2) + (v_r11);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) >> ((unsigned __int8)(a3 + 1)));
    a1 = (a2 + 1) + (a2);
    a1 = (unsigned int)((a1) & (3));
    a4 = (unsigned int)(((unsigned int)(a7)) - ((unsigned int)(*(unsigned __int16 *)(a6 + a1 * 2))));
    result = (unsigned int)((*(unsigned __int16 *)(a6 + v_r11 * 2)) * ((unsigned int)(a4)));
    result = (unsigned int)((result) - ((unsigned int)(a3)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00967B70(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, void *Arg6, uint32_t Arg7)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r11;

    local_r11 = (uint32_t)((Arg1) & (3));
    Arg2 = (Arg2) >> (3);
    Arg4 = (uint32_t)((Arg4) * ((uint32_t)((uint8_t)(Arg2))));
    Arg3 = (uint8_t)((Arg3) - ((uint8_t)(Arg4)));
    Arg2 = (Arg2) >> (1);
    Arg2 = (Arg2) + (local_r11);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) >> ((uint8_t)(Arg3 + 1)));
    Arg1 = (Arg2 + 1) + (Arg2);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg4 = (uint32_t)(((uint32_t)(Arg7)) - ((uint32_t)(*(uint16_t *)(arg6 + Arg1 * 2))));
    result = (uint32_t)((*(uint16_t *)(arg6 + local_r11 * 2)) * ((uint32_t)(Arg4)));
    result = (uint32_t)((result) - ((uint32_t)(Arg3)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0 + r11*2` | `16` | `R` |
| `Arg6` | `+ 0x0 + rcx*2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00967B70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00967B70[BB_00967B70]
  bb_00967BDA[BB_00967BDA]
```
