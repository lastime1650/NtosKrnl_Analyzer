# MiGetBestPageToZero

- RVA: `0x003200A0`–`0x0032010F` (길이 `111` bytes)
- VA: `0x00000001403200A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00075548`
- 디코드: `26`개 명령, `111/111` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00320101` → [MiSetPageZeroInProgress](../43/MiSetPageZeroInProgress_function_0043B980.md) (function, `0x0043B980`)

### Direct callers
- [MiBackgroundZeroLocalPages](../31/MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F2B1`
- [MiGetSinglePageToZero](../48/MiGetSinglePageToZero_function_00486724.md) at `0x00486832`

### Static image references
- `0x003200AD` → RVA `0x00E0A740` (`.data`; read)
- `0x003200D4` → RVA `0x00011038` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00320109` → [sub_00320214](Unknown_function_00320214.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003200A0  40 53                           push rbx
003200A2  56                              push rsi
003200A3  57                              push rdi
003200A4  41 57                           push r15
003200A6  48 81 EC B8 00 00 00            sub rsp, 0xb8
003200AD  48 8B 05 8C A6 AE 00            mov rax, qword ptr [rip + 0xaea68c]
003200B4  48 33 C4                        xor rax, rsp
003200B7  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
003200BF  41 8B F8                        mov edi, r8d
003200C2  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
003200C7  41 8B D8                        mov ebx, r8d
003200CA  C1 EF 12                        shr edi, 0x12
003200CD  33 F6                           xor esi, esi
003200CF  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
003200D4  48 8D 05 5D 0F CF FF            lea rax, [rip - 0x30f0a3]
003200DB  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
003200E0  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
003200E5  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
003200EA  83 E7 03                        and edi, 3
003200ED  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
003200F5  4C 8B FA                        mov r15, rdx
003200F8  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
003200FC  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00320101  E8 7A B8 11 00                  call 0x14043b980
00320106  48 85 C0                        test rax, rax
00320109  0F 85 05 01 00 00               jne 0x140320214
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetBestPageToZero(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;

    v_rsp = (v_rsp) - (184);
    result = (*(unsigned __int64 *)(v_rip + 11445900)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m70 = a1;
    v_rdi = (unsigned int)(((unsigned int)(a3)) >> (18));
    v_rsi = 0;
    v_stack_m98 = a2;
    v_stack_m90 = 0;
    v_stack_m78 = 0;
    v_rdi = (unsigned int)((v_rdi) & (3));
    v_stack_m80 = 1;
    v_stack_m7C = (unsigned int)((unsigned int)(a3));
    v_stack_m88 = v_rip - 3207331;
    result = MiSetPageZeroInProgress(v_stack_m98, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t MiGetBestPageToZero(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;

    local_rsp = (local_rsp) - (184);
    result = (*(uint64_t *)(v_rip + 0xAEA68C)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m70 = Arg1;
    local_rdi = (uint32_t)(((uint32_t)(Arg3)) >> (18));
    local_rsi = 0;
    v_stack_m98 = Arg2;
    v_stack_m90 = 0;
    v_stack_m78 = 0;
    local_rdi = (uint32_t)((local_rdi) & (3));
    v_stack_m80 = 1;
    v_stack_m7C = (uint32_t)((uint32_t)(Arg3));
    v_stack_m88 = v_rip - 3207331;
    result = MiSetPageZeroInProgress(v_stack_m98, Arg2, Arg3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003200A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003200A0[BB_003200A0]
```
