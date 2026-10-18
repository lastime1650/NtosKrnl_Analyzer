# RtlAreBitsClearEx

- RVA: `0x0041DBF0`–`0x0041DC42` (길이 `82` bytes)
- VA: `0x000000014041DBF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009F8F4`
- 디코드: `23`개 명령, `82/82` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiPatchDataPagesCallback](../../page/80/MiPatchDataPagesCallback_function_00806610.md) at `0x008066D9`
- [MiHotAddPartitionMemory](../../page/80/MiHotAddPartitionMemory_function_0080D5B4.md) at `0x0080D80D`
- [sub_009E5A2C](../../page/9E/Unknown_function_009E5A2C.md) at `0x009E5A6D`
- [MiMarkRetpolineBits](../../page/AA/MiMarkRetpolineBits_function_00AA0394.md) at `0x00AA03F2`
- [sub_00B1902C](../../page/B1/Unknown_function_00B1902C.md) at `0x00B1903C`
- [sub_00B1902C](../../page/B1/Unknown_function_00B1902C.md) at `0x00B19061`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0041DBFD` → [sub_0041DCD4](Unknown_function_0041DCD4.md) (`tail-transfer`)
  - `0x0041DC09` → [sub_0041DCD4](Unknown_function_0041DCD4.md) (`tail-transfer`)
  - `0x0041DC31` → [sub_0041DCD4](Unknown_function_0041DCD4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0041DBF0  48 83 EC 08                     sub rsp, 8
0041DBF4  48 8B 01                        mov rax, qword ptr [rcx]
0041DBF7  4C 8B C9                        mov r9, rcx
0041DBFA  48 3B D0                        cmp rdx, rax
0041DBFD  0F 83 D1 00 00 00               jae 0x14041dcd4
0041DC03  49 83 F8 01                     cmp r8, 1
0041DC07  77 22                           ja 0x14041dc2b
0041DC09  0F 85 C5 00 00 00               jne 0x14041dcd4
0041DC0F  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0041DC13  48 8B CA                        mov rcx, rdx
0041DC16  48 C1 EA 06                     shr rdx, 6
0041DC1A  83 E1 3F                        and ecx, 0x3f
0041DC1D  48 0F A3 0C D0                  bt qword ptr [rax + rdx*8], rcx
0041DC22  0F 93 C0                        setae al
0041DC25  48 83 C4 08                     add rsp, 8
0041DC29  C3                              ret
0041DC2A  CC                              int3
0041DC2B  48 2B C2                        sub rax, rdx
0041DC2E  49 3B C0                        cmp rax, r8
0041DC31  0F 82 9D 00 00 00               jb 0x14041dcd4
0041DC37  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0041DC3B  4D 8D 58 FF                     lea r11, [r8 - 1]
0041DC3F  4C 03 DA                        add r11, rdx
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlAreBitsClearEx(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (8);
    if (a3 > 1) goto loc_0041DC2B;
    a2 = (a2) >> (6);
    a1 = (unsigned int)((a2) & (63));
    result = (condition_is_above_or_equal) ? 1 : 0;
    v_rsp = (v_rsp) + (8);
    return result;
loc_0041DC2B:
    result = (result) - (a2);
    v_r11 = (a3 - 1) + (a2);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlAreBitsClearEx(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (8);
    if (Arg3 > 1) goto loc_0041DC2B;
    Arg2 = (Arg2) >> (6);
    Arg1 = (uint32_t)((Arg2) & (63));
    result = (condition_is_above_or_equal) ? 1 : 0;
    local_rsp = (local_rsp) + (8);
    return result;
loc_0041DC2B:
    result = (result) - (Arg2);
    local_r11 = (Arg3 - 1) + (Arg2);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041DBF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041DBF0[BB_0041DBF0]
  bb_0041DC03[BB_0041DC03]
  bb_0041DC09[BB_0041DC09]
  bb_0041DC0F[BB_0041DC0F]
  bb_0041DC2A[BB_0041DC2A]
  bb_0041DC2B[BB_0041DC2B]
  bb_0041DC37[BB_0041DC37]
  bb_0041DBF0 -->|fallthrough| bb_0041DC03
  bb_0041DC03 -->|branch| bb_0041DC2B
  bb_0041DC03 -->|fallthrough| bb_0041DC09
  bb_0041DC09 -->|fallthrough| bb_0041DC0F
  bb_0041DC2A -->|flow| bb_0041DC2B
  bb_0041DC2B -->|fallthrough| bb_0041DC37
```
