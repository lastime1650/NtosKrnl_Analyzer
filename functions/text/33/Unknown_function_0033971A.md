# sub_0033971A

- RVA: `0x0033971A`–`0x003397BB` (길이 `161` bytes)
- VA: `0x000000014033971A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076B40`
- 디코드: `32`개 명령, `161/161` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0033974C` → RVA `0x00E3D240` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00339720` → [sub_00338E63 + 0x446](Unknown_function_00338E63.md) (`tail-transfer`)
  - `0x00339766` → [sub_00338E63 + 0x823](Unknown_function_00338E63.md) (`tail-transfer`)
  - `0x00339793` → [sub_00338E63 + 0x860](Unknown_function_00338E63.md) (`tail-transfer`)
  - `0x0033979E` → [sub_00338E63 + 0x802](Unknown_function_00338E63.md) (`tail-transfer`)
  - `0x003397AD` → [sub_00338E63 + 0x17A](Unknown_function_00338E63.md) (`tail-transfer`)
  - `0x003397B6` → [sub_00338E63 + 0x1D4](Unknown_function_00338E63.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0033971A  41 BC 09 00 00 00               mov r12d, 9
00339720  E9 84 FB FF FF                  jmp 0x1403392a9
00339725  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0033972F  48 8B C0                        mov rax, rax
00339732  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00339737  48 2B C8                        sub rcx, rax
0033973A  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00339744  48 C1 F9 04                     sar rcx, 4
00339748  48 0F AF C8                     imul rcx, rax
0033974C  48 8B 05 ED 3A B0 00            mov rax, qword ptr [rip + 0xb03aed]
00339753  48 C1 E9 09                     shr rcx, 9
00339757  0F B6 54 48 01                  movzx edx, byte ptr [rax + rcx*2 + 1]
0033975C  80 E2 7F                        and dl, 0x7f
0033975F  88 94 24 A8 00 00 00            mov byte ptr [rsp + 0xa8], dl
00339766  E9 1B FF FF FF                  jmp 0x140339686
0033976B  48 8B C7                        mov rax, rdi
0033976E  49 8B CD                        mov rcx, r13
00339771  48 2B C8                        sub rcx, rax
00339774  48 8B 05 C5 3A B0 00            mov rax, qword ptr [rip + 0xb03ac5]
0033977B  48 C1 F9 04                     sar rcx, 4
0033977F  49 0F AF CE                     imul rcx, r14
00339783  48 C1 E9 09                     shr rcx, 9
00339787  0F B6 54 48 01                  movzx edx, byte ptr [rax + rcx*2 + 1]
0033978C  80 E2 7F                        and dl, 0x7f
0033978F  88 54 24 78                     mov byte ptr [rsp + 0x78], dl
00339793  E9 2B FF FF FF                  jmp 0x1403396c3
00339798  41 B8 09 00 00 00               mov r8d, 9
0033979E  E9 C2 FE FF FF                  jmp 0x140339665
003397A3  49 BF 10 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000010
003397AD  E9 2B F8 FF FF                  jmp 0x140338fdd
003397B2  41 8D 48 FF                     lea ecx, [r8 - 1]
003397B6  E9 7C F8 FF FF                  jmp 0x140339037
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0033971A(void)
{
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p78;
    unsigned __int8 v_stack_pA8;
}
```

## 5. (Beta) C Style

```c
void sub_0033971A(void)
{
    uint64_t v_stack_p40;
    uint8_t v_stack_p78;
    uint8_t v_stack_pA8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033971A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0033971A[BB_0033971A]
  bb_00339725[BB_00339725]
  bb_0033976B[BB_0033976B]
  bb_00339798[BB_00339798]
  bb_003397A3[BB_003397A3]
  bb_003397B2[BB_003397B2]
```
