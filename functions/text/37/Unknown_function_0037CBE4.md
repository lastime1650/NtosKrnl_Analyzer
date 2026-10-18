# sub_0037CBE4

- RVA: `0x0037CBE4`–`0x0037CC84` (길이 `160` bytes)
- VA: `0x000000014037CBE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B230`
- 디코드: `31`개 명령, `160/160` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0037CBEE` → RVA `0x00FC3FD0` (`.data`; read)
- `0x0037CC03` → RVA `0x00FC40E0` (`.data`; read)
- `0x0037CC2C` → RVA `0x0041FD10` (`HalpTscQueryCounterOrdered`; read)
- `0x0037CC6F` → RVA `0x00FC3FC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0037CBFD` → [sub_0037D07F](Unknown_function_0037D07F.md) (`tail-transfer`)
  - `0x0037CC0D` → [sub_0037D298](Unknown_function_0037D298.md) (`tail-transfer`)
  - `0x0037CC1E` → [sub_0037D3AC + 0xA3](Unknown_function_0037D3AC.md) (`tail-transfer`)
  - `0x0037CC36` → [sub_0037D73D + 0x14](Unknown_function_0037D73D.md) (`tail-transfer`)
  - `0x0037CC7E` → [sub_0037D37E](Unknown_function_0037D37E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0037CBE4  4C 89 68 D0                     mov qword ptr [rax - 0x30], r13
0037CBE8  41 B9 80 96 98 00               mov r9d, 0x989680
0037CBEE  4C 8B 2D DB 73 C4 00            mov r13, qword ptr [rip + 0xc473db]
0037CBF5  41 83 BD E4 00 00 00 05         cmp dword ptr [r13 + 0xe4], 5
0037CBFD  0F 85 7C 04 00 00               jne 0x14037d07f
0037CC03  4C 39 3D D6 74 C4 00            cmp qword ptr [rip + 0xc474d6], r15
0037CC0A  41 8B D9                        mov ebx, r9d
0037CC0D  0F 84 85 06 00 00               je 0x14037d298
0037CC13  41 F7 85 E0 00 00 00 00 00 01 00  test dword ptr [r13 + 0xe0], 0x10000
0037CC1E  0F 85 2B 08 00 00               jne 0x14037d44f
0037CC24  49 8B 4D 48                     mov rcx, qword ptr [r13 + 0x48]
0037CC28  49 8B 45 70                     mov rax, qword ptr [r13 + 0x70]
0037CC2C  48 8D 15 DD 30 0A 00            lea rdx, [rip + 0xa30dd]
0037CC33  48 3B C2                        cmp rax, rdx
0037CC36  0F 85 15 0B 00 00               jne 0x14037d751
0037CC3C  44 89 7D 67                     mov dword ptr [rbp + 0x67], r15d
0037CC40  0F 01 F9                        rdtscp
0037CC43  4C 8D 45 67                     lea r8, [rbp + 0x67]
0037CC47  48 C1 E2 20                     shl rdx, 0x20
0037CC4B  41 89 08                        mov dword ptr [r8], ecx
0037CC4E  48 0B D0                        or rdx, rax
0037CC51  48 8B 05 88 74 C4 00            mov rax, qword ptr [rip + 0xc47488]
0037CC58  48 B9 B8 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff780000003b8
0037CC62  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0037CC66  4C 8B 19                        mov r11, qword ptr [rcx]
0037CC69  48 F7 E2                        mul rdx
0037CC6C  4C 03 DA                        add r11, rdx
0037CC6F  48 8B 05 52 73 C4 00            mov rax, qword ptr [rip + 0xc47352]
0037CC76  4C 3B E8                        cmp r13, rax
0037CC79  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0037CC7E  0F 85 FA 06 00 00               jne 0x14037d37e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0037CBE4(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13)
{
    __int64 v_r11;

    *(unsigned __int64 *)(result - 48) = v_r13;
    *(unsigned int *)(v_rbp + 103) = (unsigned int)(v_r15);
    a2 = (v_rip + 667869) << (32);
    *(unsigned int *)(v_rbp + 103) = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12874715) + 72));
    a2 = (a2) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12874715) + 112));
    v_r11 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12874715) + 72))) + (a2);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0037CBE4(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, int64_t Arg13)
{
    int64_t local_r11;

    *(uint64_t *)(result - 0x30) = local_r13;
    *(uint32_t *)(local_rbp + 0x67) = (uint32_t)(local_r15);
    Arg2 = (v_rip + 667869) << (32);
    *(uint32_t *)(local_rbp + 0x67) = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC473DB) + 0x48));
    Arg2 = (Arg2) | (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC473DB) + 0x70));
    local_r11 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC473DB) + 0x48))) + (Arg2);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037CBE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0037CBE4[BB_0037CBE4]
  bb_0037CC03[BB_0037CC03]
  bb_0037CC13[BB_0037CC13]
  bb_0037CC24[BB_0037CC24]
  bb_0037CC3C[BB_0037CC3C]
  bb_0037CBE4 -->|fallthrough| bb_0037CC03
  bb_0037CC03 -->|fallthrough| bb_0037CC13
  bb_0037CC13 -->|fallthrough| bb_0037CC24
  bb_0037CC24 -->|fallthrough| bb_0037CC3C
```
